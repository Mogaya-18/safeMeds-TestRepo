# **Week 4 API Architecture & Needs Update.**

## **update Date: 16 th September 2026**

### **Context:**

\-            **During Week 4 OpenAPI contract development, the original \`API\_NEEDS.md\` and \`ENDPOINT\_LIST.md\` were refined to ensure technical feasibility, precise data typing, and proper mapping to implementation code.**

 

### **Updated API Needs Statements.**

1\.        MajiApp needs to read the inventory data in order to see if water purification meds are available and display that data to their suppliers.  
2\.        MajiApp needs to read customer reviews and ratings in order to suggest the best and safest water-purification products to use when purifying water and suggest the same to their suppliers.  
3\.        Water Supply App needs to receive an anonymized alert when SafeMeds detects a spike in prescriptions for waterborne illness, in order to prioritize emergency clean-water dispatch before it becomes a public health crisis  
4\.        Water supply app needs to provide a list of health professionals who can advise vendors and customers on the waterborne diseases as well as how to ensure proper water sanitation.  
5\.        Water Supply App needs to read verified pharmacies within a geographic radius to display potential community pickup points or cross-delivery hubs on their map

 

### **ENDPOINT TABLE.**

 

| METHOD | PATH | PURPOSE | MAPS TO NEED |
| :---- | :---- | :---- | :---- |
| GET | /inventory?product=chlorine-tablets\&available=true | Return available water-purification products, such as chlorine tablets, from the inventory. | MajiApp needs to read the inventory data in order to see if water purification meds are available and display that data to their suppliers |
| GET | /products/water-purification?sort=rating | Return water-purification products together with their customer ratings/reviews, ordered by rating. | MajiApp needs to read customer reviews and ratings in order to suggest the best and safest water-purification products to use when purifying water and suggest the same to their suppliers. |
| GET | /health-signals/area-alerts?region={region}\&since={date} | Return active waterborne-illness alerts for a given region  | Water Supply App needs to receive an anonymized alert when SafeMeds detects a spike in prescriptions for waterborne illness, in order to prioritize emergency clean-water dispatch before it becomes a public health crisis. |
| GET | /health-experts?type=water\_purification\&status=verified\&lat={lat}\&lng={lng}\&radius={km} | Returns the contacts of health professionals in the closest proximity. | Water supply app needs to provide a list of health professionals who can advise vendors and customers on the waterborne diseases as well as how to ensure proper water sanitation. |
| GET | /vendors?type=pharmacy\&status=verified\&lat={lat}\&lng={lng}\&radius={km}  | Return a list of verified pharmacies within a given radius of a coordinate point.  | Water Supply App needs to read verified pharmacies within a geographic radius to display potential community pickup points or cross-delivery hubs on their map. |

 

 

 

