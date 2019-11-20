import React, { useState } from "react";

import SyntaxHighlighter from "react-syntax-highlighter";
import { tomorrowNightEighties } from "react-syntax-highlighter/dist/esm/styles/hljs";

import test from "./test";
import API from "./Api";

const Component = () => {
  const [code, setCode] = useState(test);
  const handleClick = () => {
    API.call({
      service: "compile",
      success: (response: string) => {
        setCode(response);
      }
    });
  };
  return (
    <>
      <button onClick={handleClick}>Run</button>
      <SyntaxHighlighter
        style={tomorrowNightEighties}
        customStyle={{ margin: "0px" }}
      >
        {code}
      </SyntaxHighlighter>
    </>
  );
};

export default Component;
