"use client";

import { useState } from "react";
import {
  LayoutDashboard, Bot, BrainCircuit, GitGraph, Play, ShieldAlert, Workflow,
  Upload, FileCode, Zap, ChevronRight, Activity, TrendingUp, AlertTriangle,
  Cpu, Layers, Sparkles, Settings, User
} from "lucide-react";
import { cn } from "@/lib/utils";

const sidebarItems = [
  { icon: LayoutDashboard, label: "Dashboard", id: "dashboard" },
  { icon: Bot, label: "AI Agents", id: "agents" },
  { icon: BrainCircuit, label: "Knowledge Graph", id: "kg" },
  { icon: Play, label: "Test Execution", id: "execution" },
  { icon: ShieldAlert, label: "Release Intelligence", id: "releases" },
  { icon: Workflow, label: "Workflows", id: "workflows" },
  { icon: FileCode, label: "Templates", id: "templates" },
  { icon: Upload, label: "Test Packs", id: "testpacks" },
  { icon: Settings, label: "Settings", id: "settings" },
];

export default function Home() {
  const [activeTab, setActiveTab] = useState("dashboard");
  return (
    <div className="flex h-screen bg-[#0a0e1a] text-slate-200 overflow-hidden">
      <aside className="w-64 bg-[#0f1420] border-r border-slate-800 flex flex-col">
        <div className="p-6 flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-500 to-purple-600 flex items-center justify-center">
            <span className="text-white font-bold text-lg">P</span>
          </div>
          <div>
            <h1 className="font-bold text-lg text-white tracking-tight">PAIOS</h1>
            <p className="text-xs text-slate-500">AI Operating System</p>
          </div>
        </div>
        <nav className="flex-1 px-3 space-y-1">
          {sidebarItems.map((item) => (
            <button key={item.id} onClick={() => setActiveTab(item.id)}
              className={cn("w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-all",
                activeTab === item.id
                  ? "bg-cyan-500/10 text-cyan-400 border border-cyan-500/20"
                  : "text-slate-400 hover:text-slate-200 hover:bg-slate-800/50")}>
              <item.icon className="w-4 h-4" />
              {item.label}
            </button>
          ))}
        </nav>
        <div className="p-4 border-t border-slate-800">
          <div className="flex items-center gap-3 px-3 py-2">
            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
              <User className="w-4 h-4 text-white" />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-white truncate">QA Engineer</p>
              <p className="text-xs text-slate-500">Admin</p>
            </div>
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          </div>
        </div>
      </aside>
      <main className="flex-1 overflow-auto">
        <header className="h-16 border-b border-slate-800 bg-[#0f1420]/80 backdrop-blur flex items-center justify-between px-8 sticky top-0 z-10">
          <div className="flex items-center gap-2 text-sm text-slate-400">
            <span className="text-slate-500">PAIOS</span>
            <ChevronRight className="w-4 h-4" />
            <span className="text-cyan-400 capitalize">{activeTab}</span>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20">
              <div className="w-2 h-2 rounded-full bg-emerald-500" />
              <span className="text-xs text-emerald-400 font-medium">System Online</span>
            </div>
          </div>
        </header>
        <div className="p-8">
          {activeTab === "dashboard" && <DashboardView />}
          {activeTab === "agents" && <AgentsView />}
          {activeTab === "kg" && <KnowledgeGraphView />}
          {activeTab === "execution" && <ExecutionView />}
          {activeTab === "releases" && <ReleasesView />}
          {activeTab === "workflows" && <WorkflowsView />}
          {activeTab === "templates" && <TemplatesView />}
          {activeTab === "testpacks" && <TestPacksView />}
          {activeTab === "settings" && <SettingsView />}
        </div>
      </main>
    </div>
  );
}

function DashboardView() {
  const stats = [
    { label: "Total Tests", value: "4,782", change: "+12%", icon: FileCode, color: "cyan" },
    { label: "Executions", value: "18,934", change: "+8%", icon: Play, color: "emerald" },
    { label: "Active Agents", value: "6", change: "+2", icon: Bot, color: "purple" },
    { label: "Quality Score", value: "87%", change: "+3%", icon: TrendingUp, color: "amber" },
  ];
  const recentActivity = [
    { agent: "Self-Healing Engine", action: "Healed #loginBtn locator", time: "2 min ago", status: "success" },
    { agent: "Release Risk", action: "Scored PR #1287: 78/100", time: "5 min ago", status: "warning" },
    { agent: "Test Designer", action: "Generated 24 tests for checkout", time: "12 min ago", status: "success" },
    { agent: "Root Cause", action: "Classified failure as locator drift", time: "18 min ago", status: "info" },
  ];
  const moduleHealth = [
    { name: "Auth Service", health: 92 },
    { name: "Payment Service", health: 78 },
    { name: "Notification", health: 85 },
    { name: "Search", health: 94 },
    { name: "Checkout", health: 71 },
  ];
  return (
    <div className="space-y-8">
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-cyan-500/10 via-purple-500/10 to-pink-500/10 border border-slate-700 p-8">
        <div className="absolute top-0 right-0 w-64 h-64 bg-cyan-500/5 rounded-full blur-3xl" />
        <div className="relative">
          <div className="flex items-center gap-3 mb-3">
            <Sparkles className="w-5 h-5 text-cyan-400" />
            <span className="text-sm font-medium text-cyan-400">AI-Native Quality Engineering</span>
          </div>
          <h2 className="text-3xl font-bold text-white mb-2">Welcome to PAIOS</h2>
          <p className="text-slate-400 max-w-xl">The world&apos;s first AI Operating System for Quality Engineering. From automation to autonomy.</p>
        </div>
      </div>
      <div className="grid grid-cols-4 gap-4">
        {stats.map((stat) => (
          <div key={stat.label} className="bg-[#131825] border border-slate-800 rounded-xl p-5">
            <div className="flex items-center justify-between mb-3">
              <stat.icon className={cn("w-5 h-5", {
                "text-cyan-400": stat.color === "cyan",
                "text-emerald-400": stat.color === "emerald",
                "text-purple-400": stat.color === "purple",
                "text-amber-400": stat.color === "amber",
              })} />
              <span className="text-xs text-emerald-400 font-medium">{stat.change}</span>
            </div>
            <p className="text-2xl font-bold text-white">{stat.value}</p>
            <p className="text-sm text-slate-500 mt-1">{stat.label}</p>
          </div>
        ))}
      </div>
      <div className="grid grid-cols-2 gap-6">
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <Activity className="w-5 h-5 text-cyan-400" /> Agent Activity
          </h3>
          <div className="space-y-3">
            {recentActivity.map((item, i) => (
              <div key={i} className="flex items-center gap-3 p-3 rounded-lg bg-slate-800/30">
                <div className={cn("w-2 h-2 rounded-full", {
                  "bg-emerald-500": item.status === "success",
                  "bg-amber-500": item.status === "warning",
                  "bg-cyan-500": item.status === "info",
                })} />
                <div className="flex-1">
                  <p className="text-sm text-white font-medium">{item.agent}</p>
                  <p className="text-xs text-slate-400">{item.action}</p>
                </div>
                <span className="text-xs text-slate-500">{item.time}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
            <Layers className="w-5 h-5 text-purple-400" /> Module Health
          </h3>
          <div className="space-y-4">
            {moduleHealth.map((mod) => (
              <div key={mod.name}>
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-sm text-slate-300">{mod.name}</span>
                  <span className={cn("text-sm font-medium", {
                    "text-emerald-400": mod.health >= 85,
                    "text-amber-400": mod.health >= 70 && mod.health < 85,
                    "text-red-400": mod.health < 70,
                  })}>{mod.health}%</span>
                </div>
                <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div className={cn("h-full rounded-full transition-all", {
                    "bg-emerald-500": mod.health >= 85,
                    "bg-amber-500": mod.health >= 70 && mod.health < 85,
                    "bg-red-500": mod.health < 70,
                  })} style={{ width: `${mod.health}%` }} />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
        <h3 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
          <Cpu className="w-5 h-5 text-pink-400" /> System Architecture — 8 Layers
        </h3>
        <div className="grid grid-cols-4 gap-3">
          {[
            { layer: "L8", name: "Enterprise Integration", color: "from-slate-600 to-slate-700" },
            { layer: "L7", name: "Marketplace & Plugin SDK", color: "from-slate-600 to-slate-700" },
            { layer: "L6", name: "Workflow & Release Intelligence", color: "from-amber-600/50 to-amber-700/50" },
            { layer: "L5", name: "Domain Intelligence", color: "from-cyan-600/50 to-cyan-700/50" },
            { layer: "L4", name: "Knowledge & Memory", color: "from-purple-600/50 to-purple-700/50" },
            { layer: "L3", name: "Agent Framework", color: "from-pink-600/50 to-pink-700/50" },
            { layer: "L2", name: "AI Runtime", color: "from-blue-600/50 to-blue-700/50" },
            { layer: "L1", name: "Kernel", color: "from-emerald-600/50 to-emerald-700/50" },
          ].map((l) => (
            <div key={l.layer} className={cn("p-4 rounded-lg bg-gradient-to-br border border-slate-700", l.color)}>
              <span className="text-xs font-mono text-slate-400">{l.layer}</span>
              <p className="text-sm font-medium text-white mt-1">{l.name}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function AgentsView() {
  const agents = [
    { role: "Chief QA Officer", status: "Active", tasks: 3, icon: ShieldAlert, color: "text-amber-400", bg: "bg-amber-500/10" },
    { role: "Requirement Analyzer", status: "Processing", tasks: 1, icon: BrainCircuit, color: "text-cyan-400", bg: "bg-cyan-500/10" },
    { role: "Test Designer", status: "Idle", tasks: 0, icon: FileCode, color: "text-purple-400", bg: "bg-purple-500/10" },
    { role: "Self-Healing Engine", status: "Active", tasks: 2, icon: Zap, color: "text-emerald-400", bg: "bg-emerald-500/10" },
    { role: "Root Cause Intelligence", status: "Idle", tasks: 0, icon: AlertTriangle, color: "text-red-400", bg: "bg-red-500/10" },
    { role: "Release Risk", status: "Processing", tasks: 1, icon: TrendingUp, color: "text-pink-400", bg: "bg-pink-500/10" },
  ];
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-white">AI Agent Ecosystem</h2>
        <button className="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg text-sm font-medium transition-colors">
          Orchestrate Task
        </button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {agents.map((agent) => (
          <div key={agent.role} className="bg-[#131825] border border-slate-800 rounded-xl p-5 hover:border-slate-600 transition-colors">
            <div className="flex items-start justify-between mb-4">
              <div className={cn("w-10 h-10 rounded-lg flex items-center justify-center", agent.bg)}>
                <agent.icon className={cn("w-5 h-5", agent.color)} />
              </div>
              <span className={cn("text-xs px-2 py-1 rounded-full font-medium", {
                "bg-emerald-500/10 text-emerald-400": agent.status === "Active",
                "bg-amber-500/10 text-amber-400": agent.status === "Processing",
                "bg-slate-500/10 text-slate-400": agent.status === "Idle",
              })}>{agent.status}</span>
            </div>
            <h3 className="text-white font-semibold">{agent.role}</h3>
            <p className="text-sm text-slate-500 mt-1">{agent.tasks} active tasks</p>
          </div>
        ))}
      </div>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
        <h3 className="text-lg font-semibold text-white mb-4">Multi-Agent Orchestration Flow</h3>
        <div className="flex items-center justify-between">
          {["Requirement Check", "Test Selection", "Execution", "Accessibility", "Risk Report"].map((step, i) => (
            <div key={step} className="flex items-center">
              <div className="text-center">
                <div className={cn("w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-2", {
                  "bg-cyan-500/20 text-cyan-400": i <= 2,
                  "bg-slate-800 text-slate-500": i > 2,
                })}>
                  <span className="text-sm font-bold">{i + 1}</span>
                </div>
                <p className="text-xs text-slate-400">{step}</p>
              </div>
              {i < 4 && <ChevronRight className="w-5 h-5 text-slate-600 mx-4" />}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function KnowledgeGraphView() {
  const [query, setQuery] = useState("");
  const sampleQueries = [
    "Which requirements are under-tested?",
    "Which module fails most?",
    "Who owns the most failed modules?",
    "Show failure trend over time",
  ];
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white">Knowledge Graph</h2>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
        <div className="flex gap-3 mb-4">
          <input type="text" value={query} onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask the knowledge graph..."
            className="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-4 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500" />
          <button className="px-6 py-2.5 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg font-medium transition-colors">Query</button>
        </div>
        <div className="flex flex-wrap gap-2">
          {sampleQueries.map((q) => (
            <button key={q} onClick={() => setQuery(q)}
              className="text-xs px-3 py-1.5 bg-slate-800 text-slate-400 rounded-full hover:text-cyan-400 hover:bg-slate-700 transition-colors">{q}</button>
          ))}
        </div>
      </div>
      <div className="grid grid-cols-2 gap-6">
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <h3 className="text-white font-semibold mb-4">Graph Schema</h3>
          <div className="space-y-3">
            {[
              { node: "Requirement", color: "bg-blue-500", count: 1248 },
              { node: "Test", color: "bg-emerald-500", count: 4782 },
              { node: "Execution", color: "bg-amber-500", count: 18934 },
              { node: "Failure", color: "bg-red-500", count: 1256 },
              { node: "Component", color: "bg-purple-500", count: 342 },
              { node: "Owner", color: "bg-pink-500", count: 128 },
            ].map((n) => (
              <div key={n.node} className="flex items-center justify-between p-3 bg-slate-800/30 rounded-lg">
                <div className="flex items-center gap-3">
                  <div className={cn("w-3 h-3 rounded-full", n.color)} />
                  <span className="text-sm text-white">{n.node}</span>
                </div>
                <span className="text-sm text-slate-400 font-mono">{n.count.toLocaleString()}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <h3 className="text-white font-semibold mb-4">Relationships</h3>
          <div className="space-y-2 text-sm">
            {["COVERS", "EXECUTED_AS", "RESULTED_IN", "AFFECTS", "OWNED_BY", "DETECTED_IN"].map((rel) => (
              <div key={rel} className="flex items-center gap-3 text-slate-400">
                <GitGraph className="w-4 h-4 text-cyan-500" />
                <span className="font-mono text-cyan-400">{rel}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function ExecutionView() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-white">Test Execution</h2>
        <div className="flex gap-3">
          <button className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-sm font-medium transition-colors">Import Tests</button>
          <button className="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg text-sm font-medium transition-colors">Run Suite</button>
        </div>
      </div>
      <div className="bg-[#131825] border border-slate-800 rounded-xl overflow-hidden">
        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-800">
              {["Test Case", "Module", "Status", "Duration", "Last Run"].map((h) => (
                <th key={h} className="text-left text-xs font-medium text-slate-500 uppercase px-6 py-3">{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {[
              { name: "TC_001 Login with valid credentials", module: "Auth", status: "passed", duration: "2.3s", time: "2 min ago" },
              { name: "TC_002 Login with invalid password", module: "Auth", status: "passed", duration: "1.8s", time: "2 min ago" },
              { name: "TC_003 Empty username validation", module: "Auth", status: "failed", duration: "30.1s", time: "5 min ago" },
              { name: "TC_045 Add to cart flow", module: "Checkout", status: "passed", duration: "4.2s", time: "10 min ago" },
              { name: "TC_088 Checkout with 3D Secure", module: "Payment", status: "flaky", duration: "12.5s", time: "15 min ago" },
            ].map((test, i) => (
              <tr key={i} className="border-b border-slate-800/50 hover:bg-slate-800/30">
                <td className="px-6 py-3 text-sm text-white">{test.name}</td>
                <td className="px-6 py-3 text-sm text-slate-400">{test.module}</td>
                <td className="px-6 py-3">
                  <span className={cn("text-xs px-2 py-1 rounded-full font-medium", {
                    "bg-emerald-500/10 text-emerald-400": test.status === "passed",
                    "bg-red-500/10 text-red-400": test.status === "failed",
                    "bg-amber-500/10 text-amber-400": test.status === "flaky",
                  })}>{test.status}</span>
                </td>
                <td className="px-6 py-3 text-sm text-slate-400 font-mono">{test.duration}</td>
                <td className="px-6 py-3 text-sm text-slate-500">{test.time}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function ReleasesView() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white">Release Intelligence</h2>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <p className="text-sm text-slate-500 mb-1">Current Risk Score</p>
          <p className="text-4xl font-bold text-red-400">72<span className="text-lg text-slate-500">/100</span></p>
          <div className="mt-3 px-3 py-1.5 bg-red-500/10 border border-red-500/20 rounded-lg inline-block">
            <span className="text-sm text-red-400 font-medium">NO-GO</span>
          </div>
        </div>
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <p className="text-sm text-slate-500 mb-1">Tests Selected</p>
          <p className="text-4xl font-bold text-cyan-400">20<span className="text-lg text-slate-500">/342</span></p>
          <p className="text-sm text-slate-500 mt-2">Top risk-based selection</p>
        </div>
        <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
          <p className="text-sm text-slate-500 mb-1">Time Saved</p>
          <p className="text-4xl font-bold text-emerald-400">18<span className="text-lg text-slate-500">min</span></p>
          <p className="text-sm text-slate-500 mt-2">Per CI run</p>
        </div>
      </div>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
        <h3 className="text-white font-semibold mb-4">Risk Breakdown</h3>
        <div className="space-y-4">
          {[
            { factor: "Change Impact", score: 0.78, weight: "30%" },
            { factor: "Historical Failure Rate", score: 0.82, weight: "40%" },
            { factor: "Coverage Gap", score: 0.65, weight: "20%" },
            { factor: "Business Criticality", score: 1.0, weight: "10%" },
          ].map((item) => (
            <div key={item.factor}>
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-sm text-slate-300">{item.factor}</span>
                <div className="flex items-center gap-3">
                  <span className="text-xs text-slate-500">Weight: {item.weight}</span>
                  <span className="text-sm font-medium text-white">{item.score}</span>
                </div>
              </div>
              <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                <div className={cn("h-full rounded-full", {
                  "bg-red-500": item.score > 0.7,
                  "bg-amber-500": item.score > 0.4 && item.score <= 0.7,
                  "bg-emerald-500": item.score <= 0.4,
                })} style={{ width: `${item.score * 100}%` }} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function WorkflowsView() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white">Workflow Engine</h2>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-8 text-center">
        <Workflow className="w-12 h-12 text-slate-600 mx-auto mb-4" />
        <p className="text-slate-400">Workflow builder with DSL-driven orchestration</p>
        <p className="text-sm text-slate-600 mt-2">Define multi-agent quality workflows</p>
      </div>
    </div>
  );
}

function TemplatesView() {
  const templates = [
    { name: "Login Template", module: "Auth", status: "Active", tests: 12 },
    { name: "Search Template", module: "Search", status: "Active", tests: 8 },
    { name: "Checkout Template", module: "Checkout", status: "Active", tests: 24 },
    { name: "Profile Template", module: "User", status: "Inactive", tests: 6 },
  ];
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-white">Test Templates</h2>
        <button className="px-4 py-2 bg-cyan-500 hover:bg-cyan-600 text-white rounded-lg text-sm font-medium transition-colors">+ New Template</button>
      </div>
      <div className="grid grid-cols-2 gap-4">
        {templates.map((t) => (
          <div key={t.name} className="bg-[#131825] border border-slate-800 rounded-xl p-5">
            <div className="flex items-center justify-between mb-3">
              <FileCode className="w-5 h-5 text-cyan-400" />
              <span className={cn("text-xs px-2 py-1 rounded-full", {
                "bg-emerald-500/10 text-emerald-400": t.status === "Active",
                "bg-slate-500/10 text-slate-400": t.status === "Inactive",
              })}>{t.status}</span>
            </div>
            <h3 className="text-white font-semibold">{t.name}</h3>
            <p className="text-sm text-slate-500 mt-1">{t.module} &middot; {t.tests} generated tests</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function TestPacksView() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white">Test Packs</h2>
      <div className="bg-[#131825] border border-dashed border-slate-700 rounded-xl p-12 text-center">
        <Upload className="w-10 h-10 text-slate-600 mx-auto mb-4" />
        <p className="text-white font-medium mb-2">Upload Test Pack</p>
        <p className="text-sm text-slate-500 mb-4">Drag & drop Excel/CSV or click to browse</p>
        <button className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-sm transition-colors">Select File</button>
      </div>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6">
        <h3 className="text-white font-semibold mb-4">Parsed Test Cases</h3>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-slate-800">
                {["TC ID", "Module", "Scenario", "Test Data", "Status"].map((h) => (
                  <th key={h} className="text-left text-xs text-slate-500 uppercase px-4 py-2">{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {[
                { id: "TC_001", module: "Login", scenario: "Valid Login", data: "user1/pass1", status: "Parsed" },
                { id: "TC_002", module: "Login", scenario: "Invalid Password", data: "user1/wrong", status: "Parsed" },
                { id: "TC_003", module: "Login", scenario: "Empty Username", data: "/pass1", status: "Parsed" },
                { id: "TC_004", module: "Login", scenario: "Locked User", data: "lockedUser/pass1", status: "Parsed" },
              ].map((tc) => (
                <tr key={tc.id} className="border-b border-slate-800/50">
                  <td className="px-4 py-3 text-sm text-cyan-400 font-mono">{tc.id}</td>
                  <td className="px-4 py-3 text-sm text-slate-400">{tc.module}</td>
                  <td className="px-4 py-3 text-sm text-white">{tc.scenario}</td>
                  <td className="px-4 py-3 text-sm text-slate-400 font-mono">{tc.data}</td>
                  <td className="px-4 py-3">
                    <span className="text-xs px-2 py-1 rounded-full bg-emerald-500/10 text-emerald-400">{tc.status}</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

function SettingsView() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white">System Settings</h2>
      <div className="bg-[#131825] border border-slate-800 rounded-xl p-6 space-y-6">
        <div>
          <h3 className="text-white font-semibold mb-4">LLM Configuration</h3>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm text-slate-400 block mb-2">OpenAI API Key</label>
              <input type="password" placeholder="sk-..." className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
            <div>
              <label className="text-sm text-slate-400 block mb-2">Anthropic API Key</label>
              <input type="password" placeholder="sk-ant-..." className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
          </div>
        </div>
        <div className="border-t border-slate-800 pt-6">
          <h3 className="text-white font-semibold mb-4">Database Connections</h3>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-sm text-slate-400 block mb-2">PostgreSQL URL</label>
              <input type="text" placeholder="postgresql://..." className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
            <div>
              <label className="text-sm text-slate-400 block mb-2">Neo4j URI</label>
              <input type="text" placeholder="bolt://localhost:7687" className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
          </div>
        </div>
        <div className="border-t border-slate-800 pt-6">
          <h3 className="text-white font-semibold mb-4">Kernel Settings</h3>
          <div className="grid grid-cols-3 gap-4">
            <div>
              <label className="text-sm text-slate-400 block mb-2">Worker Count</label>
              <input type="number" defaultValue={4} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
            <div>
              <label className="text-sm text-slate-400 block mb-2">Max Queue Size</label>
              <input type="number" defaultValue={1000} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
            <div>
              <label className="text-sm text-slate-400 block mb-2">Task Timeout (s)</label>
              <input type="number" defaultValue={300} className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-white text-sm" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
