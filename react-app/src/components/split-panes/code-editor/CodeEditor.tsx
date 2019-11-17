import React, { useContext } from "react";
import AceEditor from "react-ace";
import { CodeContext } from "../../../contexts";

import "ace-builds/src-noconflict/mode-typescript";
import "ace-builds/src-noconflict/theme-monokai";

const CodeEditor = () => {
  const { code, ref } = useContext(CodeContext);

  // const handleCodeChange = newValue => {
  //   setCode(newValue);
  // };

  return (
    <AceEditor
      ref={ref}
      mode="typescript"
      theme="monokai"
      value={code}
      name="UNIQUE_ID_OF_DIV"
      editorProps={{ $blockScrolling: true }}
    />
  );
};

export default CodeEditor;
