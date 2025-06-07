### 2.1 Web Server

The global configuration files the configuration proxy generates need to be made available to configuration clients. The HTTP-based protocol used for downloading configuration is described in \[[PR-GCONF](#Ref_PR-GCONF)\]. Technically, the configuration consists of a set of files that are shared out using standard web server (nginx\[[1](#Ref_1)\] web server is used). The configuration processor component prepares and signs the configuration files and then copies them to the web server's output directory where they are distributed via standard means. See [Section 3.1](#31-downloading-configuration) for details on configuration distribution.



\[1\] See [*http://nginx.org/*](http://nginx.org/) for details.