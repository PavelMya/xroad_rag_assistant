### 3.5 Anti-DOS parameters: `[anti-dos]`

| **Parameter**            | **Default value** | **Description**                                                                                                                                              |
|--------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enabled                  | true              | Flag for enabling or disabling the AntiDOS system.                                                                                                           |
| max-cpu-load             | 1.1               | Maximum allowed CPU load for accepting new connections. If set to &gt; 1.0, then CPU load is not checked.                                                    |
| max-heap-usage           | 1.1               | Specifies the maximum allowed Java heap usage when accepting new connections. If set to &gt; 1.0, then heap usage is not checked.                            |
| max-parallel-connections | 5000              | Maximum number of parallel connections for AntiDOS.                                                                                                          |
| min-free-file-handles    | 100               | Minimum amount of free file handles in the system for accepting new connections. At least one free file handle must be available to accept a new connection. |