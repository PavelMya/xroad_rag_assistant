### 3.1 The Simplest Case

This scenario involves a standalone X-Road instance that is not federated with any other X‑Road instances. In this case, the simplest configuration involves one configuration source that distributes all the necessary configuration.

- private parameters (content identifier *PRIVATE-PARAMETERS*)
- shared parameters (content identifier *SHARED-PARAMETERS*) and
- optionally any additional configuration parts that are specific to this X-Road installation. *Monitoring parameters* belong to this category.

Because the shared parameters are distributed in the main configuration, the private parameters part does not contain any additional configuration sources.

![X-Road installation with single configuration source](img/pr-gconf-single-configuration-source.png)