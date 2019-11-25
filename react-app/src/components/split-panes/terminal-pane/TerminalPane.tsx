import React, { useContext } from "react";

import SyntaxHighlighter from "react-syntax-highlighter";
import { tomorrowNightEighties } from "react-syntax-highlighter/dist/esm/styles/hljs";

import { TerminalContext } from "../../../contexts/terminalContext";

const Component = () => {
  const { terminal } = useContext(TerminalContext);

  return (
    <SyntaxHighlighter
      style={tomorrowNightEighties}
      customStyle={{ margin: "0px" }}
    >
      {terminal}
    </SyntaxHighlighter>
  );
};

export default Component;
