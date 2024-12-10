code_explain_prompt="""
You are tasked with analyzing a complex legacy PLSQL codebase to generate an English explanation of its business rules 
and logic. This analysis will be used to create requirements documents for redesigning the system in a modern language 
like Java. Your goal is to extract and explain the key elements of the code in a clear, concise manner.

Here is the PLSQL code to analyze:

<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Carefully examine the provided PLSQL code and generate a comprehensive explanation of its functionality, business rules, 
and logic. Your output should be in a bullet point format, organized into the following sections:

1. Overview
   - Name of the script or module.
   - Provide a brief summary of the code's main purpose and functionality.

2. Key Components
   - List and explain the main procedures, functions, and packages in the code.
   - Describe the purpose of each component.

3. Business Rules
   - Identify and explain any business rules implemented in the code.
   - Include conditions, validations, and constraints.

4. Data Flow
   - Describe how data moves through the system.
   - Explain any data transformations or calculations.

5. Error Handling and Exceptions
   - List any error handling mechanisms or custom exceptions.
   - Explain how errors are managed and reported.

6. Database Interactions
   - Describe any database operations (SELECT, INSERT, UPDATE, DELETE).
   - Explain the purpose of these operations in the context of the business logic.

7. Integration Points
   - Identify any external system interactions or API calls.
   - Explain the purpose of these integrations.

8. Performance Considerations
   - Highlight any performance-related code, such as bulk operations or optimizations.

9. Business Logic Summary
   - Provide a concise summary of the overall business logic implemented in the code.

10. Additional Notes
    - Include any observations, potential issues, or recommendations for the redesign process.

When analyzing the code:
- If you encounter complex or unclear sections, provide your best interpretation and note any assumptions made.
- Use clear, non-technical language where possible to explain technical concepts.
- If you identify any potential issues or areas for improvement, include these in your notes.

Remember to focus on extracting the business logic and rules, rather than providing a line-by-line code explanation. 
Your analysis should help developers understand the core functionality and business requirements implemented in this 
PLSQL code, facilitating its redesign in a modern language.

Please also output the word *END* at the end of your response to indicate completion.

"""




Fun_doc_v1 = """
Convert the following PLSQL code into a detailed functional document. You are tasked with analyzing a complex legacy PLSQL codebase to generate an English explanation of its business rules 
and logic. This analysis will be used to create requirements documents for redesigning the system in a modern language 
like Java. Your goal is to extract and explain the key elements of the code in a clear, concise manner.

Here is the PLSQL code to analyze:

<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Note: Detailed explination of each and every topic. If techenical developers easily understanded. Provide higher leval of information as response.


Carefully examine the provided PLSQL code and generate a comprehensive explanation of its functionality, business rules, 
and logic. Your output should be in a bullet point format, organized into the following sections:

Purpose and Overview
   - Summarize the overall functionality and purpose of the PLSQL file, including the business problem it addresses.
   - Name of the script or module.
   - Provide a brief summary of the code's main purpose and functionality.

Functional Requirements 
   - Explain for each procedure and function in detailed,
   - Describe the expected input parameters,
   - output, and core logic.
   - Define how each function supports the larger business goal.

Data Flow
   - Describe how data moves through the system.
   - Explain any data transformations or calculations.

Error Handling and Exceptions
   - List out all type of error handling mechanisms or custom exceptions involed in the code.
   - Explain how errors are managed and reported.

Database Interactions
   - what are internally performed for the (SELECT, INSERT, UPDATE, DELETE) operations for the given PLSQL code.
   - Describe the database operations involed in the given PLSQL code. 
   - Explain the purpose of these PLSQL database operations in the context of the business logic in detailed manner.

Integration Points
   - Identify any external system interactions or API calls.
   - Explain the purpose of these integrations.

Performance Considerations
   - Highlight any performance-related code, such as bulk operations or optimizations and some other related about the performation consideration is available give the detailed explaination.

Business Logic Summary
   - Describe the Detailed explaination summary of the overall business logic implemented in the code.   
   - Please analyze the code and generate a detailed business document. 

Additional Notes
   - Include any observations, potential issues, or recommendations for the redesign process.

When analyzing the code:
- If you encounter complex or unclear sections, provide your best interpretation and note any assumptions made.
- Use clear, non-technical language where possible to explain technical concepts.
- If you identify any potential issues or areas for improvement, include these in your notes.

Remember to focus on extracting the business logic and rules, rather than providing a line-by-line code explanation. 
Your analysis should help developers understand the core functionality and business requirements implemented in this 
PLSQL code, facilitating its redesign in a modern language.

Please also output the word *END* at the end of your response to indicate completion.

"""


# Note:  
#    - Detailed explination of each and every topic.  
#    - Provide higher leval of information as response. 
#    - Carefully examine the provided PLSQL code and generate a comprehensive explanation of its functionality 
#    - Generate functional documents for all the Procedure, Modules, Triggers.. 
#    - If there is no Instruction for the any particular topic give NA 


# Note: 
#    Dont worred about the length and complexity of the code, a complete functional document for each element i needed it could be too extensive also no issues. 
#    Try to generate For all the Procedures, Modules, Triggers. Use the above template generate the output. 
  
# Instruction for the Generate complete long response output: 
#    Dont give like. Due to the extensive nature of the document and the given constraints, Repeat the same structure.  
#    Dont worred about the length and complexity of the document, a complete functional document for each element i needed it could be too extensive also no issues. 
#    we have more than one LLM calls are availbale.  
#    Everytime try to generate the Documentation.  
#    Dont worried about the within token limit try to generate. I need a complete document generate. 
#    If Incomplete response based on that it will generate the document in next call. 


Fun_doc="""
 
Convert the following PLSQL code into a detailed Functional documentation.

Input: 
   Here is the PLSQL code to analyze: 
   <plsql_code> 
      {PLSQL_CODE} 
   </plsql_code> 

Output Format: 
------------------------------------------------ 
#### **Purpose and Overview** 
      - Summarize the overall functionality and purpose of the PLSQL file, including the business problem it addresses. 
      - Name of the script or module. 
      - Provide a brief summary of the code's main purpose and functionality. 

#### **1.Procedure Name1** - Extract the procedure or function name from the PLSQL code with the numbers 
         **1.Functional Overview** - Provide a high-level summary of the procedure's functionality. 
         **2. procedure Input and Output Data** 
         Inputs: 
            Present all input parameters 
         Outputs: 
            Present all output parameters 
#### **2.Core Functionality** 
         **Processing Logic**: Describe key steps in the logic. Include validations, calculations totals, updates records.. 
         **Business Logic**: Provide details of the business rules implemented within the procedure. 
            1.Step 1 
            3.Step 2 
         **Business Rules**: Enumerate the specific conditions or rules that the procedure enforces. 
            [List it in a table] 
         **Data Validation**: Provide details of any validations applied to the input or output data. 
         **Error Codes and Messages**: Provide all error codes and corresponding messages, if any. 
              Error Code	   Description/Error Message 
              [Error_Code_1]	[Error description/message] 
              [Error_Code_2]	[Error description/message] 

#### **3.Integration Points**: 
         **Interfacing Systems**: 
            Detail all systems interfaced with the procedure. 
               [System 1: CRM, e.g., updates customer records]. 
               [System 2: ERP, e.g., sends financial summaries]. 
               
#### **4.Final Output**: 
         Describe the final result produced by the procedure, including its format and detailed structure. 

------------------------------------------------ 

Please also output the word *E-N-D* at the end of your response to indicate completion. 

Note:
   - Generate the Complete documentation please dont skip the topic, I need a complete document structure.
   - If there is no Instruction for the any particular topic give NA.
   - Each procedure add the procudure number for identify.
   - Redundant and duplicate document please dont include in the document.


"""

duplicate_redundant="""
Analyze the following PL/SQL code and identify any instances of duplicate or redundant code. The analysis should focus on locating sections of code that:

PL/SQL code:
<plsql_code>
    {PLSQL_CODE}
</plsql_code>
 
Duplicate Code:
	-Contain repeated logic, blocks, or statements that perform the same functionality multiple times.
	-Highlight areas where similar operations are implemented in multiple places.
	-Suggest ways to refactor these into reusable components (e.g., functions, procedures, or packages).

Redundant Code:
	-Include unnecessary or unused statements, variables, or operations that do not contribute to the overall functionality of the code.
	-Highlight instances where the same task is performed multiple times without adding value.
	-Identify variables, functions, or procedures that are defined but never used.

Optimization Suggestions:
	-Provide recommendations to improve the code by eliminating duplicate and redundant sections.
	-Suggest restructuring approaches to make the code more efficient and maintainable.

Following are Output Requirements:
Duplicate Code Identification:
	-Clearly list all sections of code that are duplicated, with line numbers or references for clarity.
	-Provide a brief explanation of why the code is considered duplicate and how it can be consolidated.

Redundant Code Identification:
	-List all redundant or unnecessary code sections with explanations.
	-Include any variables, constants, or procedures that are defined but not used.

Recommendations for Refactoring:
	-Suggest how to eliminate duplication, such as combining repeated logic into reusable functions or procedures.
	-Propose ways to simplify the code by removing unnecessary elements.

Output Formatting:
	-Use structured sections for clarity: Duplicate Code, Redundant Code, and Refactoring Suggestions.
	-Provide concise and actionable insights for each identified issue.

 Please also output the word */END* at the end of your response to indicate completion.
"""

java_code_gen_prompt = """

You are tasked with generating Java/Spring Boot code from legacy PLSQL code, modernizing it into a microservices 
architecture using Domain-Driven Design (DDD) concepts. Your goal is to create a fully object-oriented codebase that is 
well-structured and follows best practices for Spring Boot applications.

First, analyze the provided PLSQL code:

<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Follow these steps to convert the PLSQL code to Java/Spring Boot:

1. Identify the main functionalities and data structures in the PLSQL code.
2. Map PLSQL procedures and functions to Java methods.
3. Convert PLSQL data types to appropriate Java data types.
4. Replace PLSQL-specific constructs with Java equivalents.
5. Implement database operations using Spring Data JPA or JDBC Template.

Apply DDD concepts and microservices architecture:

1. Identify bounded contexts within the functionality.
2. Create separate microservices for each bounded context.
3. Define domain entities, value objects, and aggregates.
4. Implement repositories for data access.
5. Use domain events for communication between microservices.

Organize your code following these guidelines:

1. Use a layered architecture: Controller, Service, Repository.
2. Create separate packages for each layer and domain concept.
3. Implement dependency injection using Spring annotations.
4. Use interfaces to define contracts between layers.
5. Apply SOLID principles throughout your code.

Provide your output in the following format:

<java_code>
// Package declaration
package com.example.microservice;

// Import statements

// Class declarations, including annotations

// Method implementations
</java_code>

Include comments explaining the purpose of each class and method, especially where complex logic is involved.

Remember to handle errors appropriately and include unit tests for your Java code. Also, consider implementing API 
documentation using Swagger or Spring REST Docs.

Your final output should include multiple Java files representing the different components of the microservices 
architecture, along with a brief explanation of how the code is organized and how it implements the DDD concepts.

Please also output the word *END* at the end of your response to indicate completion.

"""

oo_design_prompt = """

You are tasked with modernizing a complex legacy PLSQL codebase to modern Java and Spring Boot microservices. Your goal 
is to generate an object-oriented design from the PLSQL code using Domain-Driven Design (DDD) principles to break the 
design into microservices. You will also create a Mermaid component diagram to visualize the architecture.

Here is the PLSQL code you need to analyze:

<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Follow these steps to complete the task:

1. Analyze the PLSQL code:
   a. Identify the main functionalities and business logic in the code.
   b. Determine the data structures and their relationships.
   c. Recognize any existing modules or logical separations in the code.

2. Apply Domain-Driven Design (DDD) principles:
   a. Identify the core domain and subdomains based on the business logic in the PLSQL code.
   b. Define bounded contexts for each subdomain.
   c. Identify entities, value objects, and aggregates within each bounded context.
   d. Determine the domain events and commands.

3. Design microservices:
   a. Map each bounded context to a potential microservice.
   b. Ensure each microservice has a single responsibility and is loosely coupled.
   c. Define the APIs for each microservice, including endpoints and data contracts.
   d. Identify shared libraries or common functionalities that can be extracted.

4. Create a Mermaid component diagram:
   a. Represent each microservice as a component.
   b. Show the relationships and dependencies between microservices.
   c. Include external systems or databases if applicable.
   d. Use appropriate Mermaid syntax for component diagrams.

5. Provide your output in the following format:
   a. Start with a brief overview of the identified domains and subdomains.
   b. List each microservice with its responsibilities and main entities.
   c. Describe the APIs for each microservice.
   d. Include the Mermaid component diagram code.
   e. Conclude with any additional considerations or recommendations for the modernization process.

Enclose your entire response within <answer> tags. Use appropriate subheadings to organize your response clearly. 
Present the Mermaid diagram code within <mermaid> tags.

Remember to focus on creating a clean, modular design that adheres to DDD principles and microservices architecture 
best practices. Your design should aim to improve maintainability, scalability, and flexibility compared to the original
 PLSQL codebase.
 
Please also output the word *END* at the end of your response to indicate completion.

"""

mermaid_code = """
You are an expert in generating Mermaid diagrams. Based on the following PL/SQL code, create a Mermaid {UML_DIAGRAM} diagram.

<plsql_code>
{PLSQL_CODE}
</plsql_code>

Provide the complete Mermaid code for this {UML_DIAGRAM} diagram.
Output only the Mermaid code. Do not include any additional text or explanations.
Ensure that the Mermaid code is valid and can be rendered correctly.

"""

Bl_logic1=""" Given the following PL/SQL code
 
<plsql_code>
    {PLSQL_CODE}
</plsql_code>
Identify and describe the business logic it implements. Break down any key operations, conditions, and calculations, and explain their purpose within the broader business process. Focus on what the code aims to achieve rather than technical syntax details """
Bl_logic2="""
I want you to generate an extremely detailed and business-oriented documentation for the following PL/SQL code. The documentation should be structured, comprehensive, and written for business stakeholders. It must clearly articulate the purpose, functionality, and potential implications of the code in a way that aligns with business goals. 

Follow these detailed guidelines to ensure the output is professional, exhaustive, and easy for business users to understand: 
<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Structure and Guidelines for the Document :

   Executive Summary 
      Begin with a concise yet comprehensive high-level overview of the code. 
      Explain the business problem or objective the code is addressing. 
      Highlight the key outcomes or benefits this code aims to deliver for the business. 

   Business Context and Relevance 
      Clearly articulate the business use case for this code. 
      Explain how the functionality aligns with specific business operations, strategies, or goals. 
      Describe the stakeholders or departments (e.g., finance, operations, HR) who would benefit from this code. 

   Functional Analysis 
      Break down the code into logical sections or modules. 
      Provide a detailed explanation of each section, focusing on what it does and its importance in achieving business objectives. 
      Highlight the workflow or sequence of processes in the code. 

   Data and Parameters in Business Terms 
      List all parameters, variables, and database objects used in the code. 
      Describe the business meaning or role of each parameter/variable. 
      For example, explain how variables represent business data like sales figures, employee details, inventory counts, etc. 

   Process Flow and Steps (Technical-to-Business Mapping) 
      Provide a step-by-step walkthrough of how the code works. 
      Map technical steps (like loops, conditions, transactions) to business processes or outcomes (e.g., data validation, reporting, compliance checks). 
      Include examples or scenarios that help illustrate real-world applications. 

   Outputs and Results 
      Detail all outputs generated by the code, such as reports, updates, or calculations. 
      Explain the business impact or value of these outputs. 
      Highlight how these outputs could be used in decision-making, strategic planning, or operational improvements. 

   Error Handling and Business Risks 
      Explain the error-handling mechanisms implemented in the code. 
      Discuss the business risks if certain conditions fail or exceptions are not handled. 
      Provide insights into how error management contributes to system reliability and operational continuity. 

   Compliance and Regulatory Alignment 
      Highlight how the code aligns with regulatory requirements (e.g., GDPR, SOX compliance). 
      Discuss any audit trails or security measures in place. 
      Emphasize how compliance is embedded within the logic of the code to avoid legal risks. 

   Scalability and Performance Considerations 
      Describe how the code can handle increasing data volumes or business growth. 
      Highlight any performance optimizations (e.g., use of indexes, efficient loops) and their importance for maintaining business efficiency. 

   Potential Enhancements and Future Opportunities 
      Suggest potential improvements or enhancements to the code. 
      Discuss how these enhancements could further align with business goals or improve outcomes. 
      Highlight any future opportunities the current code might enable. 

   Integration with Business Systems 
      Explain how the code interacts with other business systems or databases. 
      Discuss the importance of this integration for maintaining seamless operations. 
      Highlight any dependencies or prerequisites required for successful execution. 

   Business Metrics and KPIs 
      Connect the functionality of the code to measurable business metrics or KPIs (e.g., cost reduction, processing time improvement, error rate minimization). 
      Provide examples of how the code contributes to achieving these metrics. 

   Visualization and Diagrams 
      Include recommendations for adding flowcharts, diagrams, or tables that visually represent the code’s logic and its business implications. 
      Suggest ways to illustrate the data flow, dependencies, or results for improved clarity. 

   Limitations and Assumptions 
      Clearly outline any assumptions the code is based on. 
      Highlight any limitations and their potential impact on business operations. 

   Conclusion and Business Value 
      Summarize the overall importance of the code to the business. 
      Emphasize its role in improving operational efficiency, reducing risks, or supporting decision-making. 
      Conclude with a statement on how this code aligns with the business’s long-term goals.
      
      
Identify and describe the business logic it implements. Break down any key operations, conditions, and calculations, and explain their purpose within the broader business process. Focus on what the code aims to achieve rather than technical syntax details.
Please also output the word *END* at the end of your response to indicate completion.

"""

Bl_logic="""
You are the business Analyst generate the business documetation for the PL/SQL code.
I want you to generate an extremely detailed and business-oriented documentation for the following PL/SQL code.
The documentation should be structured, comprehensive, and written for business stakeholders.
It must clearly articulate the purpose, functionality, and potential implications of the code in a way that aligns with business goals.
 
The PL/SQL code is:
<plsql_code>
    {PLSQL_CODE}
</plsql_code>

Follow these detailed guidelines to ensure the output is professional, exhaustive, and easy for business users to understand: 

Structure and Guidelines for the Document

Executive Summary
	Begin with a concise yet comprehensive high-level overview of the given code. 
	Explain the business problem or objective the code is addressing. 
	Highlight the key outcomes or benefits this code aims to deliver for the business. 

Business Context and Relevance
	Clearly articulate the business use case for this code. 
	Explain how the functionality of the given code aligns with specific business operations, strategies, or goals. 
	Describe the stakeholders or departments (e.g., finance, operations, HR) who would benefit from this . 

Functional Analysis
	Break down the code into logical sections or modules. 
	Provide a detailed explanation of each section, focusing on what it does and its importance in achieving business objectives. 
	Highlight the workflow or sequence of processes in the code. 

Data and Parameters
	List all parameters, variables, and database objects used in the code. 
	Describe the business meaning or role of each parameter/variable. 
	For example, explain how variables represent business data like sales figures, employee details, inventory counts, etc. 

Process Flow and Steps
	Provide a step-by-step walkthrough of how the code works. 
	Map technical steps (like loops, conditions, transactions) to business processes or outcomes (e.g., data validation, reporting, compliance checks). 
	 
Outputs and Results
	provide the Detailed summary of output that will be generated on each module of the given code. 
	Explain the business impact or value of these outputs. 
	Highlight how these outputs could be used in decision-making, strategic planning, or operational improvements. 

Handling Business Risks
	Analyse the code and provided detailed explanation of how the business risks are handled in each and every module of the given code.
	Also provide the summary on how the business risk is handled  as a whole in the application.
	Provide insights into how risk management contributes to system reliability and operational continuity.
 
Compliance and Regulatory Alignment 
	Highlight how the code is aligned with regulatory requirements (e.g., GDPR, SOX compliance). 
	Detailed Discuss any audit trails or security measures in place. 
	Emphasize how compliance is embedded within the logic of the code to avoid legal risks. 

Scalability and Performance Considerations 
	Detailed describe how increasing data volumes or business growth is handled in this code. 
	Highlight any performance optimizations (e.g., use of indexes, efficient loops) and their importance for maintaining business efficiency. 

Potential Enhancements and Future Opportunities
	Suggest potential improvements or enhancements to the code. 
	Discuss how these enhancements could further align with business goals or improve outcomes. 
	Highlight any future opportunities the current code might enable. 

Integration with Business Systems 
	Detailed explain how the code interacts with other business systems or databases. 
	Discuss the importance of this integration for maintaining seamless operations. 
	Highlight any dependencies or prerequisites required for successful execution. 

Visualization and Diagrams
   create a Mermaid component diagram to visualize the architecture.
   - Represent each PLSQL as a modules.
   - Show the relationships and dependencies between modules.
   - Include external systems or databases if applicable.
   - Use appropriate Mermaid syntax for component diagram code.
   <mermaid>  
   graph TD
      M[Student Login] --> N(View Options)
      N --> O[View Issued Books]
      O --> P[Issued Books List]
      P --> Q[Return Book]
      Q --> O
   </mermaid> 
	
Conclusion and Business Value
	Summarize the overall importance of the code to the business. 
	Conclude with a statement on how this code aligns with the business’s long-term goals. 
 
 Please also output the word */END* at the end of your response to indicate completion.

"""


Techenical="""

I need detailed technical documentation for PL/SQL code generation.
The documentation should be structured and comprehensive, focusing on how the system is built and targeting an audience of developers, engineers, and technical teams.
The level of detail should be deep, with technical specifics to help the audience understand, use, and maintain the PL/SQL code. 

Role: You are the Technical Analyst, generate the technical documetation for the PL/SQL code.

Input:
PL/sql code:
   <plsql_code>
      {PLSQL_CODE}
   </plsql_code>

Context: 
   - I need detailed technical documentation for PL/SQL code generation.
   - The documentation should be structured and comprehensive, focusing on how the system is built and targeting an audience of developers, engineers, and technical teams.
   - The level of detail should be deep, with technical specifics to help the audience understand, use, and maintain the PL/SQL code. The documentation should also include concrete examples like API specifications, system architecture diagrams, and code annotations.
   - Provided PL/SQL codebase composed of multiple files, each containing complex technical logic implemented via PL/SQL procedures, functions, and triggers.
   - Give all the triggers, procedures, functions. dont exclude them from the output.
   

Structure and Guidelines for the Document :

Title : Technical Documentation

Introduction
	-Provide an breif overview of the document's purpose.
	-Define the scope of the documentation, including which modules, components, or systems it addresses.
	-Specify the intended audience: developers, engineers, and other technical teams.
    
Convert the following PLSQL code into a detailed Technical documentation.
 
Input:
   Here is the PLSQL code to analyze:
   <plsql_code>
      {PLSQL_CODE}
   </plsql_code>
 
Output Format:
 
#### **Purpose and Overview**
      - Summarize the overall Technical purpose of the PLSQL file, including the business problem it addresses.
      - Name of the script or module.
      - Provide a brief summary of the code's main Technical purpose.
 
#### **1.Procedure Name1** - Extract the procedure or function name from the PLSQL code with the numbers
         **1.Technical Overview** - Provide a high-level summary of the procedure's Technical functionality.
         **2. procedure Input and Output Data**
         Inputs: 
            Present all input parameters 
         Outputs: 
            Present all output parameters 
       
#### **2.Logic Flow**: 
            Processing Logic:[Describe key steps in the logic, e.g., validates data, calculates totals, updates records.] 
               - Visual Logical flow 
               - SQL Statements - Create, Insert, Update SQLs used within the procedure 
               - Data Validation  
               - Exception Handling 
                  -Error conditions & Actions 
                  -Error Codes & messages 
 
#### **3.Integration Points**:
         **Interfacing Systems**:
            Detail all systems interfaced with the procedure.
               [System 1: CRM, e.g., updates customer records].
               [System 2: ERP, e.g., sends financial summaries].

         **Dependencies**: 
               - [Table/Procedure Name: Describe dependency]. 
#### **4. Service**:
             [API/Web Service: Describe dependency] 

               
#### **5.Final Output**:
         [Summary of the Output of the procedure]
 
--------------
 
Please also output the word *E-N-D* at the end of your response to indicate completion.
 
Note:
   - Generate the Complete documentation please dont skip the topic, I need a complete document structure.
   - If there is no Instruction for the any particular topic give NA.
   - Each procedure add the procudure number for identify.
   - Redundant and duplicate document please dont include in the document.

"""

Func_overview="""
Analyze the provided PL/SQL code to generate a detailed functional document. The document should include the following sections:
   Document Title: Functional Documentation Overview
   
   Introduction:
      Provide an overview of the purpose of the PL/SQL code.
      Mention the problem it addresses or the functionality it implements.
   
   Context:
      Explain the business or technical context in which this PL/SQL code is used.
      Mention any dependencies, integrations with other systems, or prerequisites required for the code.
   
   Description:
      Break down the key components of the code, including functions, procedures, and triggers.
      Explain each component's purpose, input parameters, expected outputs, and interactions.
      Highlight any specific conditions, loops, or exceptions handled in the code.
   
   Flow Diagram:
      Create a flow diagram representing the logical flow of the PL/SQL code.
      Include key processes, decision points, inputs, and outputs to make the diagram clear and intuitive.
   
   Input:
   Accept the PL/SQL code provided and analyze it to extract relevant details for the documentation.
   PL/sql code:
      <plsql_code>
         {PLSQL_CODE}
      </plsql_code>
   
   
   Output Format:
      Provide the document in the following format:

      Introduction (1-2 paragraphs)
      Context (1-2 paragraphs)
      Description (detailed breakdown of components)
      Flow Diagram (
      Use the Mermaid code generate visual diagram.
      Note: while Generating the Mermaid code give the proper format. Like inside code dont use Parentheses brackets `()` and dont use semicolan `;`
      )

Please also output the word *E-N-D* at the end of your response to indicate completion. 

"""



# mermaid_code_detailed= """
#             Create a Mermaid diagram of type {{diagram_type}} for the provided data. Your task is to generate the Mermaid code block that represents the described diagram.
#             For the given {{content}} model class generate the proper Marmaid code for the diagram_type.
 
#             Instruction must need to follow or else diagram cant able to generate:
#             -Do not include any description, do not include the \`\`\`.
#             -Correct generated mermaid code if any syntax error present.
#             -Do not include any BLOCK STOPS
#             -Do not include any COMMAS
#             -Strictly generate mermaid code for entire input.
#             -Please make sure, only the Mermaid code block is required without any additional descriptions or code block delimiters.
           
#             - If word could be 'cart item','belongs to' means dont give space in-between need to mention as 'cartItem', 'belongsto'
#             - except the sequence diagram in mermaid code strictly dont include >>, <<, >, <. if tag will be there it wont generate the diagrams.
#             - strictly Dont include back ticks ``` and mermain in the output.
#             - Field must contains single colon only more then will remove it.
#             - If class diagram contains empty class means Strictly dont add in the mermind generating code. like class ProductNotFoundException  class ProductRepository  class SpringBootApplications
#             - dont include the Angle brackets,tags like <, >, >>, << List<Product>, Optional<Product>, ResponseEntity<Product>, <<SpringBootApplication>>, ResponseEntity<String>, ResponseEntity<?>. please dont include any open tag or close tag, Greater than sign or Less than sign  
#             - In flowchart TD Dont include '()' this kind of brackets. If include in code it wont generete diagramtic output.
#                 """

