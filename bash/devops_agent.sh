# [Install DevOps agent in local machine](https://dev.azure.com/tzather/zuhid/_settings/agentqueues?queueId=800&view=agents)

agent_file="vsts-agent-linux-x64-4.266.2.tar.gz"
mkdir -p tmp
cd tmp 
wget "https://download.agent.dev.azure.com/agent/4.266.2/${agent_file}" -O "${agent_file}"

mkdir -p myagent
tar zxvf ${agent_file} -C myagent
cd tmp/myagent
./config.sh
# sudo ./svc.sh install
# sudo ./svc.sh start
