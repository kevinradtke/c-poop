import React from "react";

import SplitPane from "react-split-pane";

import EmojiPane from "./emoji-pane/EmojiPane";
import CodeEditor from "./code-editor/CodeEditor";

import ThirdPaneTabs from "./third-pane-tabs/ThirdPaneTabs";

const SplitPanes: React.FC = () => {
  return (
    <SplitPane
      split="vertical"
      defaultSize="15%"
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
          <ThirdPaneTabs />
        </div>
      </SplitPane>
    </SplitPane>
  );
};

export default SplitPanes;
