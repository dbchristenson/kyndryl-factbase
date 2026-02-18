"""
This module defines the database models for analyzing hardware components,
vendor circularity programs, and financial/emissions metrics for Kyndryl solutions.
"""

from typing import List, Optional

from sqlalchemy import (
    INTEGER,
    REAL,
    TEXT,
    VARCHAR,
    Boolean,
    Column,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Constants for schema limits and precision
CHAR_LIMIT_SHORT = 50
CHAR_LIMIT_LONG = 255
PRECISION = 2


class Base(DeclarativeBase):
    pass


# Association table for Many-to-Many relationship between Components and Programs.
# A single component (e.g., NVIDIA H100) might be eligible for multiple programs
# (e.g., "AI Buyback" AND "Green Recycling Initiative").
component_program_association = Table(
    "component_program_association",
    Base.metadata,
    Column("component_id", ForeignKey("component.id"), primary_key=True),
    Column(
        "program_id", ForeignKey("circularity_program.id"), primary_key=True
    ),
)


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(CHAR_LIMIT_SHORT))

    # Relationships
    components: Mapped[List["Component"]] = relationship(
        back_populates="company"
    )
    programs: Mapped[List["CircularityProgram"]] = relationship(
        back_populates="company"
    )


class CircularityProgram(Base):
    """
    Stores qualitative and quantitative data on vendor specific programs.
    (e.g., HP Inspire, Cisco Refresh, IBM Global Asset Recovery)
    """

    __tablename__ = "circularity_program"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))

    name: Mapped[str] = mapped_column(VARCHAR(CHAR_LIMIT_SHORT))
    program_type: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT)
    )  # e.g., "Buyback", "Recycling", "Lease-Return"

    # Qualitative Data
    description: Mapped[str] = mapped_column(
        TEXT
    )  # Full details of the program terms
    eligibility_criteria: Mapped[str] = mapped_column(
        TEXT
    )  # What condition must the hardware be in?

    # Financial Impact Estimates (for analysis)
    avg_reimbursement_rate: Mapped[float] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )  # % of original value returned

    # Relationships
    company: Mapped["Company"] = relationship(back_populates="programs")
    eligible_components: Mapped[List["Component"]] = relationship(
        secondary=component_program_association,
        back_populates="applicable_programs",
    )


class Component(Base):
    __tablename__ = "component"

    # Basic Info
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
    name: Mapped[str] = mapped_column(VARCHAR(CHAR_LIMIT_SHORT))
    release_year: Mapped[int] = mapped_column(INTEGER)
    type: Mapped[str] = mapped_column(VARCHAR(CHAR_LIMIT_SHORT))

    # Emissions (Scope 3 Focus)
    # The raw number provided by the OEM (e.g., 1200 kgCO2e)
    pcf_value: Mapped[float] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )

    # What does that number cover?
    # specific values: "cradle_to_gate" (manufacturing only) OR "cradle_to_grave" (total life)
    pcf_boundary: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT), nullable=True
    )

    # If "cradle_to_grave", what did they assume? (e.g. "5 years use, US Grid")
    pcf_assumptions: Mapped[str | None] = mapped_column(TEXT, nullable=True)

    # Power
    # Even if you have a total PCF, you STILL need this.
    # Why? Because the vendor's "Use Phase" assumption (e.g. Global average grid)
    # is different from Kyndryl's actual deployment (New York grid).
    # You may need to 'back out' the use phase from the PCF and recalculate it
    # for New York specifically.
    power_draw_watts_tdp: Mapped[float] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )
    power_draw_watts_idle: Mapped[float | None] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )

    # Financial & TCO
    list_price_capex: Mapped[float] = mapped_column(
        REAL(precision=PRECISION)
    )  # MSRP
    is_lease_available: Mapped[bool] = mapped_column(Boolean, default=False)
    monthly_lease_opex: Mapped[float | None] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )
    lease_term_months: Mapped[int | None] = mapped_column(
        INTEGER, nullable=True
    )

    # Circularity Metric
    # e.g., 0.0 to 1.0 score based on recycled content or recyclability
    circularity_score: Mapped[float | None] = mapped_column(
        REAL(precision=PRECISION), nullable=True
    )

    # Relationships
    company: Mapped["Company"] = relationship(back_populates="components")
    applicable_programs: Mapped[List["CircularityProgram"]] = relationship(
        secondary=component_program_association,
        back_populates="eligible_components",
    )

    # Polymorphic setup
    __mapper_args__ = {
        "polymorphic_identity": "component",
        "polymorphic_on": type,
    }


class Mainframe(Component):
    __tablename__ = "mainframe"
    id: Mapped[int] = mapped_column(
        INTEGER, ForeignKey("component.id"), primary_key=True
    )

    # Mainframe specific metrics
    mips_rating: Mapped[int] = mapped_column(
        INTEGER, nullable=True
    )  # Millions of Instructions Per Second
    floor_space_sqft: Mapped[float] = mapped_column(REAL(precision=PRECISION))

    __mapper_args__ = {"polymorphic_identity": "mainframe"}


class RackServer(Component):
    __tablename__ = "rack_server"
    id: Mapped[int] = mapped_column(
        INTEGER, ForeignKey("component.id"), primary_key=True
    )

    size_u: Mapped[int] = mapped_column(
        INTEGER
    )  # Rack units (e.g., 1U, 2U, 4U)
    socket_count: Mapped[int] = mapped_column(INTEGER)  # CPU sockets

    __mapper_args__ = {"polymorphic_identity": "rack_server"}


class GPU(Component):
    __tablename__ = "gpu"
    id: Mapped[int] = mapped_column(
        INTEGER, ForeignKey("component.id"), primary_key=True
    )

    vram_gb: Mapped[int] = mapped_column(INTEGER)
    interconnect_type: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT)
    )  # e.g., NVLink, PCIe

    __mapper_args__ = {"polymorphic_identity": "gpu"}
