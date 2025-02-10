# OSCAL Compass SDK Specification

## Scope

This document specifies the functional requirements for OSCAL Compass SDK developed to work with OSCAL documents.

The keywords "MUST," "MUST NOT," "REQUIRED," "SHALL," "SHALL NOT," "SHOULD,"
"SHOULD NOT," "RECOMMENDED," "MAY," and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## Non-Goals

## Goals

## Core Functionality

### 1. Common OSCAL Extensions

*  **Rule Extension**: The SDK **MUST** define and support workflow around the OSCAL Compass RuleSet OSCAL extension.

### 2. OSCAL Validation

*   **Schema Validation:** The SDK **MUST** ensure the document adheres to the structural and data type constraints defined in the schema.
*   **Semantic Validation:** The SDK **MUST** go beyond basic schema validation to check for logical consistency and best practices.

### 3. OSCAL Transformation

*   **Data Transformation:** The tool **MUST** manipulate and transform the data within an OSCAL document.
  * Examples include:
      *   The SDK **MUST** map data between different OSCAL models (e.g., SSP to AP).

### 4. OSCAL Profile Resolution

*   **Profile Resolution:** The SDK **MUST** support the OSCAL Profile Resolution Specification