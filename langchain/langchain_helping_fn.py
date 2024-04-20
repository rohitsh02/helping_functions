# To print document properly if you want to see
def pretty_print_docs(docs):
    """This function is use to see loaded document line by line"""
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))

# Loading PDF using document loader
loader = PyPDFium2Loader("/content/660_510019001103_202210.PDF")
documents = loader.load()
document_page_contents = documents
