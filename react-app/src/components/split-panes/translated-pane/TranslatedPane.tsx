import React, { useContext } from "react";
import AceEditor from "react-ace";
import { Theme, useTheme } from "@material-ui/core/styles";

import { CodeContext } from "../../../contexts";

import "ace-builds/src-noconflict/mode-typescript";
import "ace-builds/src-noconflict/theme-monokai";

const CodeEditor = () => {
  const { translatedCode } = useContext(CodeContext);
  const theme: Theme = useTheme();
  const { fontSize } = theme.typography;

  return (
    <AceEditor
      mode="typescript"
      theme="monokai"
      value={translatedCode}
      name="UNIQUE_ID_OF_DIV_2"
      editorProps={{ $blockScrolling: true }}
      fontSize={fontSize}
      style={{ width: "100%" }}
      readOnly
    />
  );
};

export default CodeEditor;
