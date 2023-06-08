import sys
import markdown

def main():
    operation = sys.argv[1];
    
    supported_operation = ["markdown"];

    if operation not in supported_operation:
        print(f"Unsupported operation: {operation}");
        return;

    if operation == "markdown":
        input_path = input("Input-path is ");
        output_path = input("output-path is ");
        markdown_to_html_convertor(input_path, output_path);

def read_file(input_path: str) -> str:
    try:
        with open(input_path) as f:
            return f.read();
    except FileNotFoundError:
        raise Exception(f"No file found at {input_path}");

def write_file(output_path, content):
    try:
        with open(output_path, "w") as f:
            f.write(content);
    except FileNotFoundError:
        print(f"No directory found at {output_path}");

def markdown_to_html_convertor(input_path: str, output_path: str):
    md = read_file(input_path);
    html = markdown.markdown(md);
    write_file(output_path, html);

if __name__ == "__main__":
    main();
