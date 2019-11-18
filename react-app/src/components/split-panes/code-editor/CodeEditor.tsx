import React, { useContext } from "react";
import AceEditor from "react-ace";
import { Theme, useTheme } from "@material-ui/core/styles";

import { CodeContext } from "../../../contexts";

import "ace-builds/src-noconflict/mode-typescript";
import "ace-builds/src-noconflict/theme-dracula";

const CodeEditor = () => {
  const { code, ref, setCode, handleTranslation } = useContext(CodeContext);
  const theme: Theme = useTheme();
  const { fontSize } = theme.typography;

  const handleCodeChange = (newValue: any) => {
    setCode(newValue);
    handleTranslation(newValue);
  };

  return (
    <AceEditor
      ref={ref}
      mode="typescript"
      theme="dracula"
      value={code}
      name="UNIQUE_ID_OF_DIV"
      editorProps={{ $blockScrolling: true }}
      fontSize={fontSize}
      style={{ width: "100%", height: "100%" }}
      onChange={handleCodeChange}
    />
  );
};

export default CodeEditor;
