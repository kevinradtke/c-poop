import React from "react";

import FactorialExample from "./examples/factorial/FactorialExample";
import FibonnaciExample from "./examples/fibonacci/FibonnaciExample";
import FindExample from "./examples/find/FindExample";
import SortExample from "./examples/sort/SortExample";
import EmojiExample from "./examples/emoji-print/EmojiPrintExample";

import useStyles from "./documentation-tab.jss";

const DocumentationTab: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <div>
        <h3 className={classes.h3}>Example Problems</h3>
        <FactorialExample />
        <FibonnaciExample />
        <FindExample />
        <SortExample />
        <EmojiExample />
      </div>
    </div>
  );
};

export default DocumentationTab;
