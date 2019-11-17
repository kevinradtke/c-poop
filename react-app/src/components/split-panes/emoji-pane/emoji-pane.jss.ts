import { createStyles, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(() =>
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
    text: {
      fontSize: "20px"
    }
  })
);

export default useStyles;
