PATHFINDER_IDE_HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Pathfinder IDE</title>
    <link
      rel="stylesheet"
      href="https://esm.sh/@pathfinder-ide/react/dist/style.css"
    />

    <style>
      body {
        height: 100%;
        margin: 0;
        width: 100%;
        overflow: hidden;
      }

      #pathfinder {
        width: 100vw;
        height: 100vh;
      }
    </style>
  </head>

  <body>
    <div id="pathfinder"></div>
    <script type="importmap">
      {
        "imports": {
          "react": "https://esm.sh/react@18.2.0",
          "react-dom": "https://esm.sh/react-dom@18.2.0",
          "@pathfinder-ide/react": "https://esm.sh/@pathfinder-ide/react"
        }
      }
    </script>
    <script type="module">
      import React from "react";
      import ReactDOM from "react-dom";
      import { Pathfinder } from "@pathfinder-ide/react";

      const root = ReactDOM.createRoot(document.getElementById("pathfinder"));
      const fetcherOptions = {
        endpoint: window.location.origin + "/graphql",
      };

      root.render(
        React.createElement(Pathfinder, {
          fetcherOptions,
          schemaPollingOptions: {
            enabled: true,
          },
        })
      );
    </script>
  </body>
</html>
"""