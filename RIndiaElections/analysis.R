#cty   <- sf::st_read('../parliamentary-constituencies/india_pc_2014.shp', repair=TRUE)
#cty   <- readShapePoly('../parliamentary-constituencies/india_pc_2014.shp', repair=TRUE)

require(sp)
require(maptools)
require(spdplyr)
require(ggplot2)
require(data.table)
require(leaflet)
require(tibble)
require(dplyr)

# loc_st <- '../States/Admin2.shp'
# loc_pc <- '../parliamentary-constituencies/india_pc_2014.shp'
# loc_ac <- '../assembly-constituencies/India_AC.shp'

loc_ac <- '../eci/AC_Data/States/S10'
loc_pc <- '../eci/PC_Data/States/S10'

loc   <- rgdal::readOGR(loc_ac)

# loc.f <- data.table(fortify(loc))
# name  <- data.table(loc@data, row.names(loc@data))
# setnames(name, c('name', 'id'))
# loc.f   <- merge(x = loc.f, y = name, all.x=TRUE, by.x='id', by.y='id')
# loc.mid <- loc.f[, .(long=mean(long), lat=mean(lat)), by=name]


## GGPLOT
# gg <- ggplot()
# cnty.geom <- geom_map(data=loc.f, map=loc.f, aes(map_id=id, x=long, y=lat, fill=name), color='grey', size=0.25, alpha=0.5)
# cnty.text <- geom_text(data=loc.mid, aes(x=long, y=lat, label=name), color='red', size=2, alpha=1)
# cnty.dot  <- geom_point(data=loc.mid, aes(x=long, y=lat), color='blue', size=1, alpha=1)
# gg <- gg + cnty.geom
# gg <- gg + cnty.text
# gg <- gg + cnty.dot
# gg <- gg + coord_map()
# gg <- gg + labs(x="", y="")
# gg <- gg + theme(plot.background = element_rect(fill = "transparent", colour = NA),
#                  panel.border = element_blank(),
#                  panel.background = element_rect(fill = "transparent", colour = NA),
#                  panel.grid = element_blank(),
#                  axis.text = element_blank(),
#                  axis.ticks = element_blank(),
#                  legend.position = 'none')
# gg

result <- as.tibble(data.table(NO = as.factor(1:224), polls = rnorm(224)))

loc <- loc %>% 
  left_join(result)

popup <- paste0("NAME: ", loc$AC_NAME, "<br>", "Result: ", loc$polls)
pal <- colorNumeric(
  palette = "YlGnBu",
  domain = loc$polls
)

#FF6600 - bjp
#004489 - congress

## LEAFLET

leaflet(loc) %>%
  addPolygons(color = "#444444", 
              weight = 1, 
              smoothFactor = 0.5,
              opacity = 1.0, 
              fillOpacity = 0.5,
              fillColor = ~pal(polls),
              popup = popup,
              highlightOptions = highlightOptions(color = "white", weight = 2, bringToFront = TRUE))
