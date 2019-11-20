import React, { useContext } from "react";
import AceEditor from "react-ace";
import { Theme, useTheme } from "@material-ui/core/styles";

import { CodeContext } from "../../../contexts";

import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-dracula";

const CodeEditor = () => {
  const { ref, EMOJI_CODE_TEST } = useContext(CodeContext);
  const theme: Theme = useTheme();
  const { fontSize } = theme.typography;

  return (
    <AceEditor
      ref={ref}
      defaultValue={EMOJI_CODE_TEST}
      mode="python"
      theme="dracula"
      editorProps={{ $blockScrolling: true }}
      fontSize={fontSize}
      style={{ width: "100%", height: "100%" }}
    />
  );
};

export default CodeEditor;
