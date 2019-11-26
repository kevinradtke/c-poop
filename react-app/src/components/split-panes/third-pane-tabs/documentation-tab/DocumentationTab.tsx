import React from "react";

import FactorialExample from "./examples/FactorialExample";
import FibonnaciExample from "./examples/FibonnaciExample";

import useStyles from "./documentation-tab.jss";

const DocumentationTab: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <div>
        <h3 className={classes.h3}>Example Problems</h3>
        <FactorialExample />
        <FibonnaciExample />
      </div>
    </div>
  );
};

export default DocumentationTab;
