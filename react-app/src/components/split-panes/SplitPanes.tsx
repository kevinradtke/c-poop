import React from "react";

import SplitPane from "react-split-pane";

import EmojiPane from "./emoji-pane/EmojiPane";
import CodeEditor from "./code-editor/CodeEditor";
import TranslatedPane from "./translated-pane/TranslatedPane";
import TerminalPane from "./terminal-pane/TerminalPane";

const SplitPanes: React.FC = () => {
  return (
    <SplitPane
      split="vertical"
      defaultSize="20%"
      minSize={160}
      className="pane-parent"
    >
      <div className="pane pane-1">
        <EmojiPane />
      </div>
      <SplitPane split="vertical" defaultSize="60%">
        <div className="pane pane-2">
          <CodeEditor />
        </div>
        <div className="pane pane-3" style={{ overflowY: "auto" }}>
          <TranslatedPane />
          <TerminalPane />
        </div>
      </SplitPane>
    </SplitPane>
  );
};

export default SplitPanes;
