import React from "react";
import SplitPane from "react-split-pane";

import EmojiPane from "./emoji-pane/EmojiPane";
import CodeEditor from "./code-editor/CodeEditor";

const SplitPanes: React.FC = () => {
  return (
    <SplitPane
      split="vertical"
      defaultSize="20%"
      minSize={200}
      maxSize={400}
      className="pane-parent"
    >
      <div className="pane pane-1">
        <EmojiPane />
      </div>
      <SplitPane split="vertical" defaultSize="50%">
        <div className="pane pane-2">
          <CodeEditor />
        </div>
        <div className="pane pane-3">
          <>
            <button type="button">test</button>
          </>
        </div>
      </SplitPane>
    </SplitPane>
  );
};

export default SplitPanes;
