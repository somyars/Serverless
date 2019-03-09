import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    temp = req.get_json()
    output = json2xml(temp)
    if temp:
        return func.HttpResponse(
                output,mimetype='text/xml'
        )
    else:
        return func.HttpResponse(
             "Please pass a json or in the request body",
             status_code=400
        )

#Converter Code
def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)
