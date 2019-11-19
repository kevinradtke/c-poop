import React from "react";

import SyntaxHighlighter from "react-syntax-highlighter";
import { tomorrowNightEighties } from "react-syntax-highlighter/dist/esm/styles/hljs";

import test from "./test";

const Component = () => {
  return (
    <>
      <button>Run</button>
      <SyntaxHighlighter
        style={tomorrowNightEighties}
        customStyle={{ margin: "0px" }}
      >
        {test}
      </SyntaxHighlighter>
    </>
  );
};

export default Component;
