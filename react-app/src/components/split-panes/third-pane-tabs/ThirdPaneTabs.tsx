import React, { useContext } from "react";
import SwipeableViews from "react-swipeable-views";
import { makeStyles, Theme, useTheme } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";

import TranslatedPane from "../translated-pane/TranslatedPane";
import TerminalPane from "../terminal-pane/TerminalPane";
import DocumentationTab from "./documentation-tab/DocumentationTab";

import { TabsContext } from "../../../contexts/tabsContext";

interface TabPanelProps {
  children?: React.ReactNode;
  dir?: string;
  index: any;
  value: any;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
    >
      <Box p={0}>{children}</Box>
    </Typography>
  );
}

function a11yProps(index: any) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`
  };
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    backgroundColor: theme.palette.background.paper,
    width: "100%"
  }
}));

export default function FullWidthTabs() {
  const classes = useStyles();
  const theme = useTheme();
  const { value, handleChange } = useContext(TabsContext);

  return (
    <div className={classes.root}>
      <AppBar position="static" color="default">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="secondary"
          textColor="secondary"
          variant="fullWidth"
          aria-label="full width tabs example"
        >
          <Tab label="Translation" {...a11yProps(0)} />
          <Tab label="Terminal" {...a11yProps(1)} />
          <Tab label="Documentation" {...a11yProps(2)} />
        </Tabs>
      </AppBar>
      <SwipeableViews
        axis={theme.direction === "rtl" ? "x-reverse" : "x"}
        index={value}
        onChangeIndex={handleChange}
      >
        <TabPanel value={value} index={0} dir={theme.direction}>
          <TranslatedPane />
        </TabPanel>
        <TabPanel value={value} index={1} dir={theme.direction}>
          <TerminalPane />
        </TabPanel>
        <TabPanel value={value} index={2} dir={theme.direction}>
          <DocumentationTab />
        </TabPanel>
      </SwipeableViews>
    </div>
  );
}
