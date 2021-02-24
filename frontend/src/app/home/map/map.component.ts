import { AfterViewInit, Component, OnInit } from '@angular/core';
import * as L from 'leaflet';
import "leaflet-routing-machine";
import "leaflet-control-geocoder";
import "leaflet/dist/images/marker-shadow.png";
import "leaflet/dist/images/marker-icon-2x.png";


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit, AfterViewInit {
  private map;

  constructor() { }
  ngAfterViewInit(): void {
    this.initMap();
  }

  createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
  }

  private initMap(): void {
    this.map = L.map('map', {
      center: [53.4844932, -2.2535647],
      zoom: 7
    });
    const tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      minZoom: 6,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    tiles.addTo(this.map);

    // @ts-ignore 
    var geocoder = L.Control.Geocoder.nominatim();

    // geocoder.on('markgeocode', function (e) {
    //   var bbox = e.geocode.bbox;
    //   var poly = L.polygon([
    //     bbox.getSouthEast(),
    //     bbox.getNorthEast(),
    //     bbox.getNorthWest(),
    //     bbox.getSouthWest()
    //   ]).addTo(this.map);
    //   this.map.fitBounds(poly.getBounds());
    // });

    L.Routing.control({
      waypoints: [
        L.latLng(53.4844932, -2.2535647),
        L.latLng(53.6844932, -2.5535647),
        L.latLng(54.6792, -2.949)
      ],
      showAlternatives: true,
      routeWhileDragging: true,
      lineOptions: {
        styles: [{ color: '#242c81', weight: 2 }],
        extendToWaypoints: true,
        missingRouteTolerance: 1
      },
      fitSelectedRoutes: false,
      altLineOptions: {
        styles: [{ color: '#ed6852', weight: 1 }],
        extendToWaypoints: true,
        missingRouteTolerance: 1
      },
      // @ts-ignore
      // createMarker: function () { return null; },
      // @ts-ignore
      geocoder: geocoder
    })
      .on('routingstart', console.log)
      .on('routesfound', (event: L.Routing.RoutingResultEvent) => {
        let point = event.routes[0].coordinates[Math.floor((event.routes[0].coordinates).length / 2)];
        console.log(point);
        var LeafIcon2 = L.Icon.extend({
          options: {
            shadowUrl: 'https://leafletjs.com/examples/custom-icons/leaf-shadow.png',
            iconSize: [38, 95],
            shadowSize: [50, 64],
            iconAnchor: [22, 94],
            shadowAnchor: [4, 62],
            popupAnchor: [-3, -76],
            iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png'
          }
        });
        var greenIcon = new LeafIcon2();
        L.marker(point, { icon: greenIcon }).addTo(this.map);
      })
      .on('routingerror', console.log)
      .addTo(this.map);

    // this.map.on('click', function (e) {
    //   var container = L.DomUtil.create('div'),
    //     startBtn = this.createButton('Start from this location', container),
    //     destBtn = this.createButton('Go to this location', container);

    //   L.popup()
    //     .setContent(container)
    //     .setLatLng(e.latlng)
    //     .openOn(this.map);
    // });
  }

  ngOnInit(): void {
  }

}
