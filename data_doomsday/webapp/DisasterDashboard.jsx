import React, { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Bar, Line, HeatMap, Pie } from "@/components/charts"; // Custom components for viz
import axios from "axios";

export default function DisasterDashboard() {
  const [data, setData] = useState(null);
//hi
  useEffect(() => {
    axios.get("/api/disaster-insights").then((res) => setData(res.data));
  }, []);

  if (!data) return <p className="text-center mt-10">Loading data...</p>;

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold text-center">Global Disaster Risk Dashboard</h1>

      <Tabs defaultValue="risk" className="w-full">
        <TabsList className="flex justify-center gap-4 flex-wrap">
          <TabsTrigger value="risk">Top Risk Countries</TabsTrigger>
          <TabsTrigger value="correlation">Risk Correlation</TabsTrigger>
          <TabsTrigger value="prediction">2025 Forecast</TabsTrigger>
          <TabsTrigger value="climate">Climate Trends</TabsTrigger>
          <TabsTrigger value="clusters">Disaster Clustering</TabsTrigger>
          <TabsTrigger value="aid">Aid vs Impact</TabsTrigger>
        </TabsList>

        <TabsContent value="risk">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">Top 5 INFORM Risk Countries</h2>
              <Bar data={data.topRiskCountries} xKey="country" yKey="inform_risk_score" />
              <h3 className="mt-6">Disaster Counts (2000–2024)</h3>
              <Line data={data.top3DisasterTrends} xKey="year" yKeys={data.top3Countries} />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="correlation">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">Correlation of INFORM Risk with EM-DAT Data</h2>
              <HeatMap data={data.riskCorrelation} />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="prediction">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">2025 Disaster Frequency Forecast</h2>
              <Line data={data.forecasts} xKey="year" yKeys={data.forecastCountries} />
              <h3 className="mt-6">Top 5 Predictive INFORM Indicators</h3>
              <Bar data={data.featureImportance} xKey="indicator" yKey="importance" />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="climate">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">Disaster Frequency Change</h2>
              <Bar data={data.climateTrendChange} xKey="country" yKeys={["2000–2010", "2011–2024"]} />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="clusters">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">Country Clustering by Disaster Types</h2>
              <HeatMap data={data.clusters} />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="aid">
          <Card>
            <CardContent>
              <h2 className="text-xl font-semibold mb-4">Aid Distribution vs Impact</h2>
              <ScatterPlot data={data.aidVsImpact} xKey="total_affected" yKey="aid_received" colorKey="aid_per_affected" />
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
