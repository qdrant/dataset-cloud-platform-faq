from pathlib import Path

from bs4 import BeautifulSoup

#  gcp

useless_links = [
    "https://github.com/GoogleCloudPlatform/google-cloud-ruby/issues/132",
    "https://github.com/GoogleCloudPlatform/google-cloud-node/issues/329",
    "https://github.com/GoogleCloudPlatform/python-docs-samples/issues/2147",
    "https://github.com/GoogleCloudPlatform/google-cloud-node/blob/master/docs/faq.md",
    "https://cloud.google.com/appengine/docs",
    "https://cloud.google.com/blog/products/databases/spanner-relational-database-for-all-size-applications-faqs",
    "https://github.com/googleapis/google-cloud-ruby/issues/132",
    "https://cloud.google.com/tpu/docs/troubleshooting/troubleshooting",
    "https://github.com/googleapis/google-cloud-node/blob/main/docs/faq.md",
    "https://github.com/GoogleCloudPlatform/beyondcorp-applink/blob/main/faqs.md",
    "https://firebase.google.com/docs/unity/troubleshooting-faq?hl=el",
    "https://github.com/googleapis/google-cloud-node/issues/329",
    "https://cloud.google.com/blog/topics/hybrid-cloud/5-frequently-asked-questions-about-google-cloud-anthos",
    "https://cloud.google.com/dialogflow/es/docs/how/knowledge-bases",
    "https://cloud.google.com/free/docs/gcp-free-tier",
    "https://cloud.google.com/database-migration/docs/faq",
    "https://firebase.google.com/support/guides",
    "https://cloud.google.com/pubsub/docs",
    "https://github.com/GoogleCloudPlatform/gcloud-compute-ssh/blob/master/doc/faq.but",
    "https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/issues/402",
    "https://github.com/GoogleCloudPlatform/k8s-multicluster-ingress/blob/master/FAQs.md",
    "https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration",
    "https://cloud.google.com/blog/products/gcp/whats-new-with-google-cloud-resource-manager-and-other-iam-news",
    "https://cloud.google.com/compute/docs/billing-questions",
    "https://firebase.google.com/support",
    "https://firebase.google.com/pricing",
    "https://cloud.google.com/load-balancing/docs/ssl",
    "https://github.com/GoogleCloudPlatform/metacontroller/blob/master/docs/faq.md",
    "https://cloud.google.com/logging/docs/audit/troubleshooting-faq-gsuite",
    "https://cloud.google.com/dialogflow/es/docs/knowledge-connectors",
    "https://cloud.google.com/trace/docs/support",
    "https://firebase.google.com/docs/unity/troubleshooting-faq?hl=ro",
    "https://cloud.google.com/support/docs/dashboard",
    "https://cloud.google.com/blog/products/ai-machine-learning/hsbc-builds-an-internal-chatbot-to-answer-questions-on-policies",
]
links = set()
p = Path("../../data/raw/gcp/search").glob("*.html")
for path in p:
    with open(path, "r") as fd:
        soup = BeautifulSoup(fd, "html.parser")
        for a in soup.find_all("a", class_="gs-title"):
            link = a.attrs.get("href")
            if link not in useless_links:
                links.add(link)
                print(link)

print(len(links))
with open("../../data/raw/gcp/gcp_links.txt", "w") as fd:
    fd.write("\n".join(list(links)))


# tough https://cloud.google.com/datastream/docs/faq
# tough https://firebase.google.com/summit/2021/faq
# tough https://firebase.google.com/docs/perf-mon/troubleshooting?platform=ios
# tough https://firebase.google.com/docs/android/troubleshooting-faq
# tough https://firebase.google.com/docs/android/troubleshooting-faq?hl=ro
# tough https://firebase.google.com/docs/perf-mon/troubleshooting?platform=web&hl=sr
# tough https://firebase.google.com/docs/crashlytics/troubleshooting?platform=android&hl=BG
# tough https://firebase.google.com/docs/ios/troubleshooting-faq?hl=sr
# tough https://firebase.google.com/docs/crashlytics/troubleshooting?platform=ios
