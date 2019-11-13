import { createStyles, Theme, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: "100%",
      position: "relative",
      overflow: "auto",
      height: "100%"
    },
    listSection: {
      backgroundColor: "#192734"
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
