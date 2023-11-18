APOLLO_SANDBOX_HTML = """
        <div id="sandbox" style="position:absolute;top:0;right:0;bottom:0;left:0"></div>
        <script
         src="https://embeddable-sandbox.cdn.apollographql.com/_latest/embeddable-sandbox.umd.production.min.js">
         </script>
        <script>
         new window.EmbeddedSandbox({
           target: "#sandbox",
           // Pass through your server href if you are embedding on an endpoint.
           // Otherwise, you can pass whatever endpoint you want Sandbox to start up with here.
           initialEndpoint: window.location.origin + "/graphql",
         });
         // advanced options: https://www.apollographql.com/docs/studio/explorer/sandbox#embedding-sandbox
        </script>
    """