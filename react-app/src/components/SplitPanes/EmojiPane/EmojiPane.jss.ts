import { createStyles, Theme, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: "100%",

      // backgroundColor: theme.palette.background.paper,
      position: "relative",
      overflow: "auto",
      height: "100%"
    },
    listSection: {
      backgroundColor: "inherit"
    },
    ul: {
      backgroundColor: "inherit",
      padding: 0
    },
    nested: {
      paddingLeft: theme.spacing(6)
    },
    avatar: {
      backgroundColor: "transparent"
    },
    text: {
      fontSize: "20px"
    }
  })
);

export default useStyles;
