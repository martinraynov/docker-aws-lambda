# docker-aws-lambda
An example on lambda usage with the official image from amazon

We can test the lambda using this curl command : 

```
curl -XPOST "http://lambda.local.io/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
```