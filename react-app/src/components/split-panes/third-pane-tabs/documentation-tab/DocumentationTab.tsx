import React, { useContext } from "react";

import AceEditor from "react-ace";
import { Theme, useTheme } from "@material-ui/core/styles";
import { TranslatedContext } from "../../../../contexts/translatedContext";

import "ace-builds/src-noconflict/theme-monokai";

const DocumentationTab: React.FC = () => {
  const { translatedCode } = useContext(TranslatedContext);
  const theme: Theme = useTheme();
  const { fontSize } = theme.typography;
  return (
    <div style={{ backgroundColor: "#2F3129" }}>
      <div>
        <h3 style={{ marginTop: "0px", paddingTop: "16px" }}>
          Example Problems
        </h3>
        <h4>1) Factorial</h4>

        <AceEditor
          mode="python"
          theme="monokai"
          value={translatedCode}
          editorProps={{ $blockScrolling: true }}
          fontSize={fontSize - 2}
          style={{ height: "200px" }}
          readOnly
        />
      </div>
    </div>
  );
};

export default DocumentationTab;
