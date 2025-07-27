from pydantic import Field
from fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E., regarding the structural integrity of the condenser tower. Key  points include material fatigue analysis and maintenance history.",
    "report.pdf": "The report details the state of a 20m condenser tower, including its operational efficiency, recent inspections, and recommendations for future upgrades to improve performance.",
    "financial.docx": "This document outlines the project's budget and expenditures, including a breakdown of costs for materials, labor, and contingency funds. It also highlights areas where cost overruns have occurred.",
    "outlook.pdf": "This document presents the projected future performance of the system, including expected output, maintenance schedules, and potential risks. It also includes a comparison with industry benchmarks.",
    "plan.md": "The plan outlines the steps for the project's implementation, including timelines, resource allocation, and key milestones. It also identifies potential bottlenecks and mitigation strategies.",
    "spec.txt": "These specifications define the technical requirements for the equipment, including material properties, dimensions, and performance criteria. It also includes compliance with industry standards and certifications.",
    "meeting_notes.txt": "Notes from the project kickoff meeting held on July 15, 2025. Topics discussed include project scope, team assignments, and initial deadlines. Action items were assigned to team leads for follow-up.",
    "risk_assessment.docx": "This document evaluates potential risks associated with the project, including financial, operational, and environmental risks. It provides a risk matrix and mitigation strategies for each identified risk.",
    "design_review.pdf": "The design review document includes feedback from stakeholders on the initial design. It highlights areas for improvement, such as structural reinforcements and cost optimizations.",
    "timeline.xlsx": "A detailed project timeline, including Gantt charts for each phase of the project. It specifies start and end dates, dependencies, and resource allocations.",
    "user_manual.md": "The user manual provides step-by-step instructions for operating the system. It includes troubleshooting tips, maintenance schedules, and safety precautions.",
    "case_study.pdf": "A case study analyzing a similar project completed in 2023. It discusses lessons learned, challenges faced, and how they were overcome.",
    "contract.docx": "The contract outlines the terms and conditions between the client and the contractor. It includes payment schedules, deliverables, and penalties for delays.",
    "environmental_report.pdf": "This report assesses the environmental impact of the project, including emissions, waste management, and compliance with regulations. It also suggests measures to minimize the environmental footprint.",
    "training_materials.pptx": "Slides for training sessions on using the new system. Topics include system overview, key features, and troubleshooting common issues."
}


@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string"
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]


@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string"
)
def edit_document(
    doc_id:str = Field(description="Id of the document that will be edited"),
    old_str:str = Field(description="The text to replace. Must match exactly, including white space"),
    new_str: str = Field(description="The new text to insert in the place of the old text")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)

    
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]


@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format"
)
def format_document(
    doc_id: str=Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.
    
    The id of the document you need to reformat is:
    <document_id>
    {doc_id}
    </document_id>
    
    Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
    Use the 'edit_document' tool to edit the document. After the document has been reformatted...
    """
    
    return [base.UserMessage(prompt)]
    
    
@mcp.prompt(
    name="summarize",
    description="Summarize the contents of the document"
)
def summarize_document(
    doc_id: str=Field(description="Id of the document to summarize")
) -> list[base.Message]:
    prompt =f"""
    Your goal is to summarize a document
    
    The id of the document you need to summarize is:
    <document_id>
    {doc_id}
    </document_id>
    
    Make the summarization detailed, clear, and concise. Feel free to add to any missing gaps of information.
    Use the 'edit_document' tool to edit the document. After the document has been summarized...
    """

    return [base.UserMessage(prompt)]


if __name__ == "__main__":
    mcp.run(transport="stdio", log_level="ERROR")
