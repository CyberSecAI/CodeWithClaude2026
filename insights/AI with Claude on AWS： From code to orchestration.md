# AI with Claude on AWS: From code to orchestration

## Executive Summary
Antonio Rodriguez from AWS discusses the "Better Together" partnership between AWS and Anthropic. The session focuses on transitioning Claude-powered applications from local prototypes to production-ready cloud environments using Amazon Bedrock. Key themes include the massive compute infrastructure investment (Project Reindeer), specialized chips (Trainium), and the security, scalability, and compliance advantages of running Claude on AWS.

## Key Points
- **Infrastructure Investment:** Amazon has invested multi-billions in Anthropic, building Project Reindeer, one of the largest AI compute infrastructures for training and hosting Claude models.
- **Custom Chipsets:** AWS uses purpose-built Trainium chips for cost-effective and high-speed model inference.
- **Bedrock Platform Features:** Beyond models, Bedrock offers evaluation, prompt optimization, fine-tuning (exclusive for Haiku), knowledge bases for RAG, and guardrails for content filtering and PII masking.
- **Security & Privacy:** AWS ensures zero operator access and data residency within specific boundaries (e.g., GDPR compliance by deploying only in European regions).
- **Three Ways to Use Claude on AWS:**
    1. **Amazon Bedrock:** Direct API access with AWS-native security and integration.
    2. **Claude Platform on AWS:** The native Anthropic experience with consolidated AWS billing and IAM controls.
    3. **Claude Desktop/Co-work:** Connecting desktop tools directly to Bedrock or the AWS-hosted platform.
- **Orchestration:** Integration with AWS Bedrock Agent Core for hosting agents securely, compatible with frameworks like LangChain, CrewAI, and the Claude Agent SDK.

## Notable Quotes
- "We are really just whispering models these days, not really writing code."
- "A story about teamwork, a story about better together."
- "No one from Amazon or from Anthropic can actually get access to those instances. Your data remains fully private."
- "It is all about asking Claude to configure itself."

## Takeaways
- Use Amazon Bedrock if you need tight integration with AWS security, IAM, and compliance frameworks (HIPAA, FedRAMP).
- Leverage the Claude Platform on AWS for the latest Anthropic features while maintaining consolidated AWS billing.
- Explore Project Reindeer and Trainium infrastructure to scale Claude applications cost-effectively.
- Use the provided AWS workshops to learn about team standards, cost control, and agent orchestration.
