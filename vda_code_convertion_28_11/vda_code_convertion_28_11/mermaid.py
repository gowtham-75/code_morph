import re
mermaid_js = "https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js"

def generateDiagram(mermaid_diagram_code):

    downloadMermaidDiagram = """
            <div style="text-align: center;">
            <button onclick="downloadMermaidDiagram()">Download Diagram</button>
            <script>
            function downloadMermaidDiagram() {
                const diagramElement = document.getElementById('mermaid-diagram');

                mermaid.initialize({ startOnLoad: false });  
                mermaid.init(diagramElement); 

                const svgData = diagramElement.querySelector('svg').outerHTML;
                const blob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'mermaid_diagram.svg';
                link.click();
            }
            </script>"""

    html_string = f"""
            <script src="{mermaid_js}"></script>
            <div class="mermaid" id="mermaid-diagram" style="text-align:center;">
            {mermaid_diagram_code}
            </div>
            <br>
            <br>
            """+downloadMermaidDiagram
    return html_string

def generateDiagram1(mermaid_diagram_code):
 
    html_string = f"""
        <script src="{mermaid_js}"></script>
        <div class="mermaid" id="mermaid-diagram" style="text-align:center;">
                {mermaid_diagram_code}
        </div>
        <br>
        <br>
                """
    return html_string

def generate_mermaid_process_flow_chart(text):
#     pattern = re.compile(r'flowchart LR(.+?)(?=(flowchart LR|```|$))', re.DOTALL | re.IGNORECASE)
    pattern = re.compile(r'flowchart LR(.+?)(?=(</mermaid>|```|$))', re.DOTALL | re.IGNORECASE)
    # Find all matches
    matches = pattern.findall(text)
    # Extract just the matched group
    extracted_data = [match[0].strip() for match in matches if match[0].strip()]
    return extracted_data
 
def generate_mermaid_process_flow_chart_TD(text):
#     pattern = re.compile(r'flowchart TD(.+?)(?=(flowchart TD|```|$))', re.DOTALL | re.IGNORECASE)
    
    pattern = re.compile(r'flowchart TD(.+?)(?=(</mermaid>|```|$))', re.DOTALL | re.IGNORECASE)
    # Find all matches
    matches = pattern.findall(text)
    # Extract just the matched group
    extracted_data = [match[0].strip() for match in matches if match[0].strip()]
    return extracted_data

def generate_mermaid_process_flow_chart_graph(text):
#     pattern = re.compile(r'flowchart LR(.+?)(?=(flowchart LR|```|$))', re.DOTALL | re.IGNORECASE)
    pattern = re.compile(r'graph LR(.+?)(?=(</mermaid>|```|$))', re.DOTALL | re.IGNORECASE)
    # Find all matches
    matches = pattern.findall(text)
    # Extract just the matched group
    extracted_data = [match[0].strip() for match in matches if match[0].strip()]
    return extracted_data
 
def generate_mermaid_process_flow_chart_TD_graph(text):
#     pattern = re.compile(r'flowchart TD(.+?)(?=(flowchart TD|```|$))', re.DOTALL | re.IGNORECASE)
    
    pattern = re.compile(r'graph TD(.+?)(?=(</mermaid>|```|$))', re.DOTALL | re.IGNORECASE)
    # Find all matches
    matches = pattern.findall(text)
    # Extract just the matched group
    extracted_data = [match[0].strip() for match in matches if match[0].strip()]
    return extracted_data


def generate_mermaid_component(text):
#     pattern = re.compile(r'flowchart TD(.+?)(?=(flowchart TD|```|$))', re.DOTALL | re.IGNORECASE)
    
    pattern = re.compile(r'componentDiagram(.+?)(?=(</mermaid>|```|$))', re.DOTALL | re.IGNORECASE)
    # Find all matches
    matches = pattern.findall(text)
    # Extract just the matched group
    extracted_data = [match[0].strip() for match in matches if match[0].strip()]
    return extracted_data