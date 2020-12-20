import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Accordion from "@material-ui/core/Accordion";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import AccordionSummary from "@material-ui/core/AccordionSummary";
// import AccordionActions from "@material-ui/core/AccordionActions";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
// import Divider from "@material-ui/core/Divider";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";

const useStyles = makeStyles((theme) => ({
  heading: {
    fontSize: theme.typography.pxToRem(15),
  },
  secondaryHeading: {
    fontSize: theme.typography.pxToRem(15),
    color: theme.palette.text.secondary,
  },
  icon: {
    verticalAlign: "bottom",
    height: 20,
    width: 20,
  },
  details: {
    alignItems: "center",
  },
  column: {
    flexBasis: "63.33%",
  },
  helper: {
    borderLeft: `2px solid ${theme.palette.divider}`,
    padding: theme.spacing(1, 2),
  },
  link: {
    color: theme.palette.primary.main,
    textDecoration: "none",
    "&:hover": {
      textDecoration: "underline",
    },
  },
}));

export default function Sidebar({ edges, selected, setSelected }) {
  const classes = useStyles();
  const handleChange = (panel) => (event, isExpanded) => {
    setSelected(isExpanded ? panel : false);
  };

  return (
    <div style={{ overflowY: "scroll", maxHeight: "100vh", maxWidth: "40%" }}>
      {edges.map((edge, index) => {
        return (
          // <div className={classes.root}>
          <div>
            <Accordion
              style={{ borderRadius: "0px" }}
              expanded={selected === index}
              onChange={handleChange(index)}
            >
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1c-content"
                id="panel1c-header"
              >
                <div className={classes.column}>
                  <Typography className={classes.heading}>
                    {edge.address1.split(",")[0]}
                  </Typography>
                </div>
                <div className={classes.column}>
                  <Typography className={classes.secondaryHeading}>
                    Elevation: {edge.elevation}
                    <br />
                    Distance: {edge.distance}
                  </Typography>
                </div>
              </AccordionSummary>
              <AccordionDetails className={classes.details}>
                <div className={classes.column}>
                  <Card className={classes.root}>
                    <CardActionArea>
                      <img
                        src={`https://maps.googleapis.com/maps/api/streetview?location=${edge.p1[1]},${edge.p1[0]}&size=400x400&key=AIzaSyCshXjseDpk7gzKTHR4iZg2TN_kkFlgsHM`}
                      />
                      <CardContent>
                        <Typography gutterBottom>
                          Starting location: {edge.address1}
                          <br />
                          <br />
                          Ending location: {edge.address2}
                        </Typography>
                        <Typography
                          variant="body2"
                          color="textSecondary"
                          component="p"
                        >
                          {edge.p1[0]}, {edge.p1[1]}
                        </Typography>
                      </CardContent>
                    </CardActionArea>
                    <CardActions>
                      <Button
                        size="small"
                        color="primary"
                        onClick={() => {
                          window.open(
                            `http://maps.google.com/maps?q=${edge.p1[1]},${edge.p1[0]}`,
                            "_blank"
                          );
                        }}
                      >
                        Take me there
                      </Button>
                    </CardActions>
                  </Card>
                </div>
              </AccordionDetails>
            </Accordion>
          </div>
        );
      })}
    </div>
  );
}
