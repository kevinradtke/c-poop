import React, { useState, useContext } from "react";

import SyntaxHighlighter from "react-syntax-highlighter";
import { tomorrowNightEighties } from "react-syntax-highlighter/dist/esm/styles/hljs";

import { TranslatedContext } from "../../../contexts";

import API from "./Api";

const Component = () => {
  const { translatedCode } = useContext(TranslatedContext);
  const [terminal, setTerminal] = useState("$");

  const handleClick = () => {
    API.call({
      service: "compile",
      method: "post",
      params: { code: translatedCode },
      success: (response: string) => {
        setTerminal(response);
      }
    });
  };

  return (
    <>
      <button onClick={() => handleClick()}>Run</button>
      <SyntaxHighlighter
        style={tomorrowNightEighties}
        customStyle={{ margin: "0px" }}
      >
        {terminal}
      </SyntaxHighlighter>
    </>
  );
};

export default Component;
