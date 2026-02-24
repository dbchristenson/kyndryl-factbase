"""
This module defines the database models for analyzing
hardware components, vendor circularity programs, and
financial/emissions metrics for Kyndryl solutions.
"""

from typing import List

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
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

# Constants for schema limits and precision
CHAR_LIMIT_SHORT = 50
CHAR_LIMIT_LONG = 255
PRECISION = 2


class Base(DeclarativeBase):
    pass


# Association table for Many-to-Many relationship
# between Components and Programs.
# A single component (e.g., NVIDIA H100) might be
# eligible for multiple programs
# (e.g., "AI Buyback" AND "Green Recycling Initiative").
component_program_association = Table(
    "component_program_association",
    Base.metadata,
    Column(
        "component_id",
        ForeignKey("component.id"),
        primary_key=True,
    ),
    Column(
        "program_id",
        ForeignKey("circularity_program.id"),
        primary_key=True,
    ),
)


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        info={
            "label": "Vendor Name",
            "description": (
                "The company or manufacturer name."
            ),
        },
    )

    # Relationships
    components: Mapped[List["Component"]] = relationship(
        back_populates="company"
    )
    programs: Mapped[
        List["CircularityProgram"]
    ] = relationship(back_populates="company")


class CircularityProgram(Base):
    """
    Stores qualitative and quantitative data on
    vendor specific programs.
    (e.g., HP Inspire, Cisco Refresh,
    IBM Global Asset Recovery)
    """

    __tablename__ = "circularity_program"

    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"),
        info={
            "label": "Vendor",
            "description": (
                "The vendor offering the program."
            ),
        },
    )

    name: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        info={
            "label": "Program Name",
            "description": (
                "The name of the circularity program."
            ),
        },
    )
    program_type: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        info={
            "label": "Program Type",
            "description": (
                "Category of program "
                "(e.g., Buyback, Recycling, "
                "Lease-Return)."
            ),
        },
    )

    # Qualitative Data
    description: Mapped[str] = mapped_column(
        TEXT,
        info={
            "label": "Description",
            "description": (
                "Full details of the program terms."
            ),
        },
    )
    eligibility_criteria: Mapped[str] = mapped_column(
        TEXT,
        info={
            "label": "Eligibility Criteria",
            "description": (
                "What condition must the hardware "
                "be in to qualify?"
            ),
        },
    )

    # Financial Impact Estimates (for analysis)
    avg_reimbursement_rate: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Avg Reimbursement Rate",
            "description": (
                "Percentage of original value "
                "returned (0.0 to 1.0)."
            ),
        },
    )

    # Relationships
    company: Mapped["Company"] = relationship(
        back_populates="programs"
    )
    eligible_components: Mapped[
        List["Component"]
    ] = relationship(
        secondary=component_program_association,
        back_populates="applicable_programs",
    )


class Component(Base):
    __tablename__ = "component"

    # Basic Info
    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("company.id"),
        info={
            "label": "Vendor",
            "description": (
                "The manufacturer providing "
                "the component."
            ),
        },
    )
    name: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        info={
            "label": "Product Name",
            "description": (
                "The specific model name "
                "(e.g., z16, H100)."
            ),
        },
    )
    release_year: Mapped[int] = mapped_column(
        INTEGER,
        info={
            "label": "Release Year",
            "description": (
                "Used to calculate vintage "
                "and efficiency gains."
            ),
        },
    )
    product_family: Mapped[
        str | None
    ] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        nullable=True,
        info={
            "label": "Product Family",
            "description": (
                "Groups generations together "
                "(e.g., 'IBM z', 'Power E', "
                "'ThinkSystem SR'). Used for "
                "filtering/grouping "
                "generational queries."
            ),
        },
    )
    type: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT)
    )

    # Emissions (Scope 3 Focus)
    pcf_value: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Reported Emissions (kgCO2e)",
            "description": (
                "The raw carbon footprint number "
                "provided by the vendor."
            ),
        },
    )

    pcf_boundary: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        nullable=True,
        info={
            "label": "Emissions Scope",
            "description": (
                "Does the reported number include "
                "use-phase? (Cradle-to-Gate vs. "
                "Cradle-to-Grave)."
            ),
        },
    )

    pcf_assumptions: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
        info={
            "label": "Emissions Assumptions",
            "description": (
                "If Cradle-to-Grave, what "
                "grid/usage did they assume?"
            ),
        },
    )

    # Power
    power_draw_watts_tdp: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Max Power (Watts TDP)",
            "description": (
                "Thermal Design Power. Used to "
                "calculate worst-case "
                "Scope 2 emissions."
            ),
        },
    )
    power_draw_watts_typical: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Typical Power (Watts)",
            "description": (
                "Typical operating power draw "
                "in watts. Represents realistic "
                "workload power, not worst-case "
                "TDP or best-case idle. "
                "Denominator for efficiency "
                "calculations."
            ),
        },
    )
    power_draw_watts_idle: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Idle Power (Watts)",
            "description": (
                "Power draw at idle. Used for "
                "realistic Scope 2 estimates."
            ),
        },
    )

    # Financial & TCO
    list_price_capex: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        info={
            "label": "List Price (CAPEX)",
            "description": (
                "Upfront purchase cost (MSRP)."
            ),
        },
    )
    is_lease_available: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        info={
            "label": "Lease Available?",
            "description": (
                "Is an As-a-Service / lease "
                "option offered? (TRUE/FALSE)."
            ),
        },
    )
    monthly_lease_opex: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Monthly Lease (OPEX)",
            "description": (
                "Cost per month if leased "
                "(As-a-Service model)."
            ),
        },
    )
    lease_term_months: Mapped[
        int | None
    ] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "Lease Term (Months)",
            "description": (
                "Duration of the lease "
                "agreement in months."
            ),
        },
    )

    # Circularity Metric
    circularity_score: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Circularity Score (0-1)",
            "description": (
                "Internal metric: "
                "1.0 = Fully Recyclable/Circular."
            ),
        },
    )

    # Relationships
    company: Mapped["Company"] = relationship(
        back_populates="components"
    )
    applicable_programs: Mapped[
        List["CircularityProgram"]
    ] = relationship(
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
        INTEGER,
        ForeignKey("component.id"),
        primary_key=True,
    )

    # Mainframe specific metrics
    mips_rating: Mapped[int] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "MIPS (Performance)",
            "description": (
                "Millions of Instructions Per "
                "Second (Mainframe specific)."
            ),
        },
    )
    msu_rating: Mapped[
        int | None
    ] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "MSU Rating",
            "description": (
                "Million Service Units — IBM's "
                "standard capacity/licensing "
                "metric. More stable than MIPS "
                "for cross-generational "
                "comparison."
            ),
        },
    )
    num_cps: Mapped[int | None] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "Number of CPs",
            "description": (
                "Number of configurable Central "
                "Processors (CPs). Required "
                "for per-core efficiency "
                "normalization."
            ),
        },
    )
    num_ifls: Mapped[
        int | None
    ] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "Number of IFLs",
            "description": (
                "Number of Integrated Facility "
                "for Linux engines. Tracks "
                "Linux-dedicated capacity "
                "separately."
            ),
        },
    )
    floor_space_sqft: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        info={
            "label": "Floor Space (sqft)",
            "description": (
                "Physical footprint of the "
                "mainframe in square feet."
            ),
        },
    )

    __mapper_args__ = {
        "polymorphic_identity": "mainframe",
    }


class RackServer(Component):
    __tablename__ = "rack_server"
    id: Mapped[int] = mapped_column(
        INTEGER,
        ForeignKey("component.id"),
        primary_key=True,
    )

    size_u: Mapped[int] = mapped_column(
        INTEGER,
        info={
            "label": "Rack Size (U)",
            "description": (
                "Rack units (e.g., 1U, 2U, 4U)."
            ),
        },
    )
    socket_count: Mapped[int] = mapped_column(
        INTEGER,
        info={
            "label": "Socket Count",
            "description": (
                "Number of CPU sockets "
                "in the server."
            ),
        },
    )
    num_cores: Mapped[
        int | None
    ] = mapped_column(
        INTEGER,
        nullable=True,
        info={
            "label": "Total CPU Cores",
            "description": (
                "Total physical CPU cores. "
                "Needed for per-core efficiency "
                "normalization."
            ),
        },
    )
    benchmark_score: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Benchmark Score",
            "description": (
                "Performance score from a "
                "standardized benchmark. The "
                "throughput numerator for "
                "efficiency calculations."
            ),
        },
    )
    benchmark_type: Mapped[
        str | None
    ] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        nullable=True,
        info={
            "label": "Benchmark Type",
            "description": (
                "Identifies which benchmark "
                "standard was used (e.g., "
                "'SPECint_rate2017', "
                "'SPECpower_ssj2008', "
                "'TPC-C'). Only compare rows "
                "with matching benchmark_type."
            ),
        },
    )

    __mapper_args__ = {
        "polymorphic_identity": "rack_server",
    }


class GPU(Component):
    __tablename__ = "gpu"
    id: Mapped[int] = mapped_column(
        INTEGER,
        ForeignKey("component.id"),
        primary_key=True,
    )

    vram_gb: Mapped[int] = mapped_column(
        INTEGER,
        info={
            "label": "VRAM (GB)",
            "description": (
                "Video Memory size "
                "(Critical for AI model weights)."
            ),
        },
    )
    tflops_fp16: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "TFLOPS (FP16)",
            "description": (
                "Half-precision floating-point "
                "throughput (TFLOPS). Primary "
                "AI inference performance "
                "metric."
            ),
        },
    )
    tflops_fp32: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "TFLOPS (FP32)",
            "description": (
                "Single-precision floating-point "
                "throughput (TFLOPS). Standard "
                "compute performance metric."
            ),
        },
    )
    interconnect_type: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        info={
            "label": "Interconnect",
            "description": (
                "Speed of connection between "
                "chips (e.g., NVLink, PCIe)."
            ),
        },
    )

    __mapper_args__ = {
        "polymorphic_identity": "gpu",
    }
