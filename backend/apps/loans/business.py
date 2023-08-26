from apps.loans.models import LoanRequest


def create_loan_request(data):
    #{'questions': [OrderedDict([('label', 'Nome'), ('value', 'Arthur'), ('file', <InMemoryUploadedFile: suap.png (image/png)>)])]}
    questions = data.get("response")

    for question in questions:
        if "file" not in question.keys():
            continue
        file = question.get("file", None)
        if file:
            # store and get path
            pass
            question["value"] = "filepath"

        question.pop("file")
        
    
    loan_request = LoanRequest.objects.create(response=questions)
    return loan_request
