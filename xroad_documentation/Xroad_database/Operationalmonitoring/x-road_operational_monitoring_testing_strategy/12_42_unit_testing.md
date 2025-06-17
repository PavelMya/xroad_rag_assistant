### 4.2 Unit Testing

Generally, unit tests are used for testing the behaviour of single units of code (functions, methods) with clearly defined inputs and outputs.

The required coverage and scope of unit tests have not been defined for this project. Thus, unit tests will be written for units of code that implement protocols, conversion between data formats etc, including tests against invalid or unexpected input. Such units of code will be isolated for testability.

For larger components that are used for control logic, system-wide data exchange as well as configuration, unit tests are not justified and will not be written. The behaviour and error handling of such components will be covered by automated or manual integration tests.

Unit tests will not be written for third-party protocol implementations (such as JMXMP).