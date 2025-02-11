# OSCAL Compass SDK Specification

<details>
<summary>Table of Contents</summary>

<!-- toc -->
- [OSCAL Compass SDK Specification](#oscal-compass-sdk-specification)
  - [Scope](#scope)
  - [Goals](#goals)
    - [Multi-Language Support](#multi-language-support)
    - [Usabilty](#usabilty)
  - [Core Functionality](#core-functionality)
    - [1. OSCAL Support](#1-oscal-support)
    - [2. OSCAL Extensions Support](#2-oscal-extensions-support)
    - [3. OSCAL Validation](#3-oscal-validation)
    - [4. OSCAL Transformation](#4-oscal-transformation)
    - [5. OSCAL Profile Resolution](#5-oscal-profile-resolution)
  - [Future Consideration](#future-consideration)
<!-- tocstop -->

</details>

## Scope

This document specifies the functional requirements for OSCAL Compass SDK developed to work with OSCAL documents.

The keywords "MUST," "MUST NOT," "REQUIRED," "SHALL," "SHALL NOT," "SHOULD,"
"SHOULD NOT," "RECOMMENDED," "MAY," and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## Goals

### Multi-Language Support

* **Functionality Consistency:** Offer a functionally consistent developer experience across all supported languages.
* **Language-Specific Idioms:**  Each SDK should adhere to the conventions and best practices of its target language.

### Usabilty

* **Ease of Use:**  Provide an intuitive API for developers to interact with OSCAL data.
* **Versioning:** Each SDK **MUST** follow semantic versioning to clearly communicate changes and ensure compatibility.
* **Extensibility**: Offer mechanisms for developers to customize with alternate implementations, while providing sensible defaults.

Each SDK **SHOULD** have comprehensive documentation, including:

* **API Reference:**  Detailed documentation of all classes, methods, and functions. This could be generated from code comments.
* **User Guide:**  Tutorials and examples to help developers get started with the SDK.
* **Code Samples:**  Provide boilerplate code examples demonstrating common use cases.

## Core Functionality

### 1. OSCAL Support

* **OSCAL Schema:** Support the official [OSCAL](https://pages.nist.gov/OSCAL/) schema definitions.
* **OSCAL Data Formats**
  * SDKs **MUST** support the JSON format
  * SDKs **MAY**  support XML and YAML formats.

### 2. OSCAL Extensions Support

*  **RuleSet Extension**: The SDK **MUST** define the OSCAL Compass `RuleSet` OSCAL extension in the target language.
   *  The SDK **MUST** provide support for parsing and indexing rule information for OSCAL `Components`.

### 3. OSCAL Validation

*   **Schema Validation:** The SDK **MUST** ensure the document adheres to the structural and data type constraints defined in the official OSCAL schemas.
*   **Semantic Validation:** The SDK **SHOULD** go beyond basic schema validation to check for logical consistency and best practices.  
    **Examples include:**
      *   **Duplicate UUIDs**: Identify duplicate UUID in OSCAL models.
      *   **Reference Validation**: All references in responsible parties are found in roles.
      *   **Links Validation**: All UUIDs in links and prose match resources in backmatter

### 4. OSCAL Transformation

*   **Data Transformation:** The SDK **MUST** provide transformation workflows for the data within an OSCAL document.  
    **Examples include:**
      *   The SDK **MUST** map data between different OSCAL models including:
          *   Profile to Catalog: See [OSCAL Profile Resolution](#5-oscal-profile-resolution)
          *   Component Definition to SSP
          *   Component Definition to Assessment Plan - **OPTIONAL**
          *   SSP to Assessment Plan
          *   Assessment Plan to Assessment Results
      *   The SDK **MAY** map data between OSCAL and other data structures (e.g. XCCDF)

### 5. OSCAL Profile Resolution

*   **Profile Resolution:** The SDK **MUST** support the [OSCAL Profile Resolution Specification](https://pages.nist.gov/OSCAL/resources/concepts/processing/profile-resolution/)

## Future Consideration

* **Conformance Testing:**  Once the SDKs mature, specification conformance testing should be added to ensure each required use case is covered and the OSCAL inputs and outputs are consistent.