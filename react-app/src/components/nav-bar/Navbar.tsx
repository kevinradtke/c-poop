import React, { useContext } from "react";

import { TranslatedContext, TerminalContext } from "../../contexts/";

import { AppBar, Button, Toolbar, Typography } from "@material-ui/core/";

import useStyles from "./navbar.jss";

const Navbar: React.FC = () => {
  const classes = useStyles();

  const { handleTranslation } = useContext(TranslatedContext);
  const { handleTerminal } = useContext(TerminalContext);

  return (
    <div className={classes.root}>
      <AppBar position="static" elevation={2} className={classes.appbar}>
        <Toolbar>
          <Typography variant="h5" className={classes.title}>
            {"C"}
            <span role="img" aria-label="title-poop-emoji">
              {"💩 "}
            </span>
            {"Compiler"}
          </Typography>
          <Button
            variant="outlined"
            onClick={() => handleTranslation()}
            className={classes.translateButton}
          >
            Translate
          </Button>
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => handleTerminal()}
          >
            Run
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Navbar;
