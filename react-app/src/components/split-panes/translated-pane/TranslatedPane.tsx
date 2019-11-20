import React, { useContext } from "react";
import AceEditor from "react-ace";
import { Theme, useTheme } from "@material-ui/core/styles";

import { TranslatedContext } from "../../../contexts";

import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-monokai";

const CodeEditor = () => {
  const { translatedCode } = useContext(TranslatedContext);
  const theme: Theme = useTheme();
  const { fontSize } = theme.typography;

  return (
    <AceEditor
      mode="python"
      theme="monokai"
      value={translatedCode}
      name="UNIQUE_ID_OF_DIV_23"
      editorProps={{ $blockScrolling: true }}
      fontSize={fontSize}
      style={{ width: "100%" }}
      readOnly
    />
  );
};

export default CodeEditor;
