## Cloud Platforms FAQ Dataset

Cloud Platforms FAQ Dataset contains pairs of question and answers parsed from sites of popular
cloud providers such as [AWS](https://aws.amazon.com/), [Azure](https://azure.microsoft.com/en-us/), [Hetzner](https://www.hetzner.com/) and others.

In the first place it was collected to be used in our [demo](https://github.com/qdrant/demo-cloud-faq).

This repository contains source code of parsers which were used to fetch the data.

The dataset can be downloaded via the following command:

```shell
wget -O cloud_faq_dataset.jsonl https://storage.googleapis.com/demo-cloud-faq/dataset/cloud_faq_dataset.jsonl
```
