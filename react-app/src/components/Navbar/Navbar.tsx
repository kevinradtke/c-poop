import React from "react";

import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";

import useStyles from "./navbar.jss";

const Navbar: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" elevation={2}>
        <Toolbar>
          <Typography variant="h5" className={classes.title}>
            {"C"}
            <span role="img" aria-label="title-poop-emoji">
              {"💩 "}
            </span>
            {"Compiler"}
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Navbar;
