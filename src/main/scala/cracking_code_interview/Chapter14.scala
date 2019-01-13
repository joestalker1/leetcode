package cracking_code_interview

//14.1
//select tenantId from tenants t1 join tenantApartment t2 on t1.tenantId == t2.tenantId
//group by t1.tenant having count(t1.tenantId) > 1

//14.2
//select b.bulding,req.status from (select b.buildingId,b.buildingName from buildings b) t inner join request req on t.buildingId == req.buildingId

//14.3
//update requests r set r.status='close'
//where r.appId in (select a.apptId,b.buildingName from appartment a join buildings b on a.buildingId = b.buildingId)