### Few-shot: tiny inventory → plan
Input:
[
  {"app_name":"erp","cpu_cores":2,"ram_gb":4,"db_engine":"postgres","rpo_min":15,"rto_min":30}
]
Good plan output (concise):
{
  "apps":[
    {
      "name":"erp",
      "target":{
        "compute":{"service":"ec2","instance_type":"t3.small"},
        "database":{"service":"rds","engine":"postgres","size":"db.t4g.micro"},
        "storage":{"service":"s3","bucket":"cloudlift-demo-erp"}
      },
      "estimated_monthly_usd": 52.4,
      "rpo_rto":{"rpo_minutes":15,"rto_minutes":30}
    }
  ]
}