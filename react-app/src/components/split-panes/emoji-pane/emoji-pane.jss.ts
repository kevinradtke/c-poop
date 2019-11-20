import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: "100%",
      position: "relative",
      overflow: "auto",
      height: "100%"
    },
    listSection: {
      backgroundColor: theme.palette.primary.dark
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
