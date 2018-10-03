import wap
import urllib
import json

server = 'http://api.wolframalpha.com/v1/query.jsp'
appid = 'TUYAJ5-P4J8PKKJ4W'
input = 'who are you?'

waeo = wap.WolframAlphaEngine(appid, server)
query = waeo.CreateQuery(input)
result = waeo.PerformQuery(query)
waeqr = wap.WolframAlphaQueryResult(result)
jsonresult = waeqr.JsonResult()

print jsonresult
x = json.loads(jsonresult)
print '-'
print x[-1][-1][-1][-1]
