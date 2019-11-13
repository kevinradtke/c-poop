import React from "react";
import SplitPane from "react-split-pane";

import EmojiPane from "./EmojiPane/EmojiPane";

const SplitPanes: React.FC = () => (
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
      <div className="pane pane-2">IDE</div>
      <div className="pane pane-3">Translated IDE</div>
    </SplitPane>
  </SplitPane>
);

export default SplitPanes;
